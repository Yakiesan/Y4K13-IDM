chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === "send_to_engine") {
    // This connects to the name defined in nmh-manifest.json
    chrome.runtime.sendNativeMessage('com.y3k14.download', 
      { url: request.url }, 
      (response) => {
        console.log("Response from Engine:", response);
      }
    );
  }
});