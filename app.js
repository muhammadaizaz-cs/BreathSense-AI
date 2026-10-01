let recordBtn = document.getElementById("recordBtn");
let statusText = document.getElementById("status");
let audioPlayer = document.getElementById("audioPlayer");

let mediaRecorder;
let chunks = [];

recordBtn.onclick = async () => {

  let stream = await navigator.mediaDevices.getUserMedia({ audio: true });

  mediaRecorder = new MediaRecorder(stream);
  mediaRecorder.start();

  statusText.innerText = "Recording...";

  mediaRecorder.ondataavailable = e => chunks.push(e.data);

  mediaRecorder.onstop = () => {
    let blob = new Blob(chunks, { type: "audio/wav" });
    let url = URL.createObjectURL(blob);

    audioPlayer.src = url;
    chunks = [];

    statusText.innerText = "Recording complete";
  };

  setTimeout(() => mediaRecorder.stop(), 15000);
};