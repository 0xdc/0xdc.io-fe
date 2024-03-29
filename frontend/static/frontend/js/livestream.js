var livestream = function(uid){
	'use strict';

	// check the existance of the hls playlist
	// if found, place a video widget on the page
	var header = document.querySelector("header");
	fetch("https://"+uid+"/api/status")
	.then(response => {
		if (!response.ok) {
			throw new Error("http response not okay. not doing anything");
		}
		return response.json();
	})
	.then(data => {
		if (!data['online']) {
			throw new Error("stream is offline. skipping");
		}

		var url = "https://"+uid+"/hls/stream.m3u8";

		var video = document.createElement("video");
		video.controls = true;
		video.muted = true;

		if (video.canPlayType("application/vnd.apple.mpegurl")) {
			// native support
			// load the video and go
			video.src = url;
			header.prepend(video);
			video.play();
		} else if (Hls.isSupported()) {
			// using hls.js
			var hls = new Hls();
			hls.loadSource(url);
			hls.attachMedia(video);
			hls.on(Hls.Events.MANIFEST_PARSED, () => {
				header.prepend(video);
				video.play();
			})
		}
	})
	.catch(() => {
		console.log("fetch() returned error. not doing anything...");
	});
};

document.addEventListener('DOMContentLoaded', function(){
	livestream(user);
});
