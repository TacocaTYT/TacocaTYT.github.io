const rpb = document.getElementById("recentPostButton");

const postTitle = "404";
fetch("news/posts/")
    .then(response => response.text())
    .then((data) => console.log(data));

const postURL = "404.html";


rpb.textContent = postTitle;
rpb.href = postURL;