function addDownloadButton() {
    const players = document.querySelectorAll('video');
    players.forEach(player => {
        if (player.parentElement.querySelector('.y3k14-btn')) return;
        
        let btn = document.createElement('div');
        btn.className = 'y3k14-btn';
        btn.innerText = 'Download with Y3K14';
        btn.style = "position:absolute; z-index:9999; background:#00D084; color:black; cursor:pointer; padding:5px; font-weight:bold; top:10px; right:10px;";
        
        btn.onclick = () => {
            chrome.runtime.sendMessage({ action: "download", url: window.location.href });
        };
        player.parentElement.appendChild(btn);
    });
}
setInterval(addDownloadButton, 2000);