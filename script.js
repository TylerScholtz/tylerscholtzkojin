
var navbar = document.getElementById('navbar');
var hamburger = document.getElementById('hamburger');

hamburger.addEventListener('click', function() {
    navbar.style.display = navbar.style.display === 'none' ? 'flex' : 'none';
});



var typed = new Typed(".intro p", {
  strings: ["Welcome to my personal website! This is a platform where I document my journey in coding, specifically with projects like GPT chatbots and my travel blogs from Japan. Feel free to explore and learn more about my journey. You can also check out the Github repository for this website.", "タイラーの個人ウェブサイトへようこそ！ ここは、GPTチャットボットや日本の旅行ブログなどのプロジェクトに関連したコーディングの旅を文書化するプラットフォームです。 自由に探索して、私の旅についてもっと学んでください。 また、このウェブサイトのGithubリポジトリも見ることができます."],
  typeSpeed: 30
});