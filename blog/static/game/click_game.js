var score = 0;

$(document).ready(function() {

    // 定时器定时获取新的物品信息并显示在面板上
    setInterval(getNewItem, 2000);

    // 单击物体后，物体消失并加分
    $('#game-board').on('click', '.item', function() {
      $(this).remove();
      score++;
      $("#score").text(score);
    });
});

function getNewItem() {
    $.getJSON('/api/get_new_item/', function(item) {
        var leftPos = item['x'];
        var topPos = item['y'];
        var color = item['color'];

        var newItem = $('<div class="item"></div>');
        newItem.css('position', 'absolute');
        newItem.css('left', leftPos + 'px');
        newItem.css('top', topPos + 'px');
        newItem.css('background-color', color);
        newItem.css('width', '50px');
        newItem.css('height', '50px');

        $('#game-board').append(newItem);
    });
}