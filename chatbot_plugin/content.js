// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
    	console.dir($);
      $('p.text-text-muted').html("<a href=\"chatterbot.org\">Click Here To Open ChatBot</a>");
    }
  }
);

