document.addEventListener("DOMContentLoaded", function() {
  const countdownElement = document.getElementById("countdown");
  const targetDate = new Date("2023-04-29T09:00:00+0900");

  function updateCountdown() {
    const now = new Date();
    const remainingTime = targetDate - now;

    if (remainingTime <= 0) {
      countdownElement.textContent = "記念祭が始まりました！";
      return;
    }

    const days = Math.floor(remainingTime / (1000 * 60 * 60 * 24));
    const hours = Math.floor((remainingTime % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

    countdownElement.textContent = `記念祭開始まで${days}日${hours}時間${minutes}分${seconds}秒！`;
  }

  updateCountdown();
  setInterval(updateCountdown, 1000);
});
