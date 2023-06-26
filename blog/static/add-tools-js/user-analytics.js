// 从本地存储中获取统计数据
var pageviews = localStorage.getItem('pageviews') || 0;
var uniqueVisits = localStorage.getItem('uniqueVisits') ? JSON.parse(localStorage.getItem('uniqueVisits')).length : 0;
var likes = localStorage.getItem('likes') || 0;
var visitedPages = localStorage.getItem('visitedPages') ? JSON.parse(localStorage.getItem('visitedPages')) : [];

// 渲染统计数据到前端页面上
document.getElementById('pageviews').textContent = pageviews;
document.getElementById('uniqueVisits').textContent = uniqueVisits;
document.getElementById('likes').textContent = likes;
visitedPages.forEach(function(page) {
  var li = document.createElement('li');
  li.textContent = page;
  document.getElementById('visitedPages').appendChild(li);
});
