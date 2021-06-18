<%*
/*
# Hypothes.idian  a templater script for retrieving annotations from Hypothes.is
Dev: RoamHacker https://twitter.com/roamhacker

# Prerequisites:
+ Templater plugin by https://github.com/SilentVoid13/Templater
+ Free Hypothes.is developer token from: https://hypothes.is/account/developer
  + This script will prompt you for his token and save it to a file called "hypothesis config.md"
  + This file store your configuration and can be located any where in your vault.
  + Since it contains your unique user token, you should not share this file with others.

# Features:
+ Retrieve your annotations for a web article/web PDF'
+ Retrieve your annotations from a date
+ Open a URL in hypothes.is for annotation
+ Retrieve ALL user annotations for a web article/web PDF

# Output:
+ If an empty document, descriptive front matter is output to beginning of the document, followed by annotations
+ If document already contains text, the annotations are inserted at the current location

# Update Log:
+ 2021-05-04 fix that they config file can be located anywhere
+ 2021-04-26 First alpha version released to testers
*/

const configFileName = 'hypothesis config.md';
let userToken = '';
let userid    = '';
const apiUrl = 'https://api.hypothes.is/api/';

const apiHTTPGet = async (apiCall, data) => {
  return await fetch(apiCall, {
    "method": "GET", cache: 'no-cache',
    "headers": { "Authorization": "Bearer " + userToken }
  }).then(async(data)=> await data.json() )
}

const getAllAnnotations = async (articleUrl)=> {
	const searchUrl = `search?limit=200&order=asc&uri=${encodeURIComponent(articleUrl)}`;
	const results = await apiHTTPGet(`${apiUrl}${searchUrl}`);
  return await apiAnnotationSimplify(results);
}

const getMyAnnotations = async (articleUrl)=> {
	const searchUrl = `search?limit=200&user=${userid}&order=asc&uri=${encodeURIComponent(articleUrl)}`;
	const results = await apiHTTPGet(`${apiUrl}${searchUrl}`);
  return await apiAnnotationSimplify(results);
}

const getAnnotationsSinceDate = async (fromDate)=> {
  const searchUrl = `search?limit=200&user=${userid}&sort=updated&order=asc&search_after=${encodeURIComponent(fromDate)}`;
  const results = await apiHTTPGet(`${apiUrl}${searchUrl}`);
  return await apiAnnotationSimplify(results);
}

const apiAnnotationSimplify = async (results)=>{
  return results.rows.map(e=>{
    var r = {
      title: e.document.title[0], uri:e.uri, context: e.links.incontext,
      text: e.text, highlight: '', tags: e.tags,
      user: e.user, group:e.group,  created: e.created, updated: e.updated,
    };
    try {
      if(e.target[0].selector) {
        var txt = e.target[0].selector.filter(e=>e.type=='TextQuoteSelector');
        if(txt) r.highlight = txt[0].exact;
      }
    } catch(e){};
    return r;
  });
}

const openArticleInHypothesis = async (articleUrl)=> {
  window.open('https://via.hypothes.is/' + articleUrl, '_blank');
}

const getUserProfile = async ()=> await apiHTTPGet(`${apiUrl}profile`);

const configFile = await app.vault.getFiles().find(f => f.name == 'hypothesis config.md');

//Setup configuration file
if (configFile == undefined ) {
  userToken = await tp.system.prompt("Hypothes.is user token from https://hypothes.is/account/developer");
  console.log(userToken)
  if (userToken==null || userToken.length==0) return;
  const userProfile = await getUserProfile();
  userid = userProfile.userid;
  if( userToken.length>0 && userid != null ){
      const fileOutput = `---\nhypothesisUserToken: ${userToken} \n` +
     `hypothesisUserID: ${userid} \n` +
      `---\n\nThis file can be place anywhere in your vault.\n\n` +
      `get your token here: https://hypothes.is/account/developer`
      await app.vault.create(configFileName,fileOutput);
  }
} else {
  //load user  token
  if (app.metadataCache.metadataCache[ app.metadataCache.fileCache[configFile.path].hash ]?.frontmatter?.hypothesisUserToken) {
    userToken = app.metadataCache.metadataCache[ app.metadataCache.fileCache[configFile.path].hash ].frontmatter.hypothesisUserToken;
    userid    = app.metadataCache.metadataCache[ app.metadataCache.fileCache[configFile.path].hash ].frontmatter.hypothesisUserID;
  }
}

if(userToken.length == 0 || userid == null) {
  new Notice(`No user token or is invalid. Try deleting ${configFileName} and restarting the script.`)
  return '';
}

const selectedText = tp.file.selection();
let articleAnnotations = null;
let articleURL = null;
let insertUser = false;
//find out the type of action
const hypothesisAction = await tp.system.suggester(
  [ 'Retrieve my annotations for a web article/web PDF',
    'Retrieve my annotations from a date',
    'Open URL in Hypothes.is for annotation (select a URL or type url)',
    'Retrieve ALL annotations for a web article/web PDF',
  ],
  ['myarticle', 'mydate', 'openURL', 'allAnnotations'])

switch (hypothesisAction) {
  case 'myarticle':
    articleURL = await tp.system.prompt('URL:', selectedText);
    if(articleURL==null ||  articleURL.length==0) return '';
    articleAnnotations = await getMyAnnotations(articleURL);
    break;
  case 'allAnnotations':
    articleURL = await tp.system.prompt('URL:', selectedText);
    if(articleURL==null ||  articleURL.length==0) return '';
    articleAnnotations = await getAllAnnotations(articleURL);
    insertUser = true;
    break;
  case 'openURL':
    const articleURLtoOpen = await tp.system.prompt('URL to open in Hypothes.is:', selectedText );
    await openArticleInHypothesis(articleURLtoOpen);
    return;
    break;
  case 'mydate':
    const articleDates = await tp.system.prompt('Retrieve article titles  from date:', tp.date.now('YYYY-MM-DD', -7) );
    if(articleDates==null || articleDates.length==0) return '';
    articleAnnotations = await getAnnotationsSinceDate(articleDates);
    if (articleAnnotations.length==0) {
      new Notice('no results for this date range');
      return;
    }
    const articlesNames = [...new Set( articleAnnotations.map(e=>e.title + ' \n(' + e.uri + ')' ))];
    const articlesURIs  = [...new Set( articleAnnotations.map(e=>e.uri))];
    articleURL = await tp.system.suggester(articlesNames, articlesURIs)
    if(articleURL==null || articleURL.length==0) return '';
    articleAnnotations = await getMyAnnotations(articleURL);
    break;
}

if (articleAnnotations==null || articleAnnotations.length == 0) return '';

/* TEMPLATE STARTS HERE */
if (tp.file.content.length==0) {
  //likely a new document, insert front matter
  tR += `---\n`;
  tR += `fileType: HypothesisAnnotations\n`;
  tR += `creationDate: ${tp.date.now('YYYY-MM-DD')} \n`;
  tR += `annotationDate: ${articleAnnotations[0].created.substring(0,10)}\n`;
  tR += `uri: ${articleAnnotations[0].uri}\n`;
  tR += `---\n`;
}

tR += `# ${articleAnnotations[0].title}\n`
tR += `URL: ${articleAnnotations[0].uri}\n\n`

for( a of articleAnnotations) {
  let tags = '';
  let user = '';
  if(a.tags.length>0) tags = ' ' + (a.tags.map(t=> '#'+ t)).join(' ');
  if(insertUser) user = ' _(' + a.user.replace('acct:','').replace('@hypothes.is','') + ')_';
  tR += `> ${a.highlight}${tags}${user}\n`;
  if(a.text) tR += `+ ${a.text}\n`;
  tR += `\n`;
}
%>
