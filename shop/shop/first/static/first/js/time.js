let time = 4;
const countDownEl = document.getElementById("countdown");

setInterval(updateCountdown, 1000);

function updateCountdown(){
	const minutes = Math.floor(time / 60);
	let seconds = time % 60;
	countDownEl.innerHTML = `Страница закроется через ${seconds}`;
	if (time!= 0) {
		time--;
	}
	else{
		document.location.assign('../../')
	}
	console.log(seconds);
}
