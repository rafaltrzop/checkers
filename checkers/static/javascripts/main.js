$(document).ready(function () {
  bind_events();
});

function bind_events() {
  var current_position = undefined;
  var destination = undefined;

  $('td').click(function () {
    if ($(this).find('.board__piece').length) {
      current_position = {
        x: $(this).data('x'),
        y: $(this).data('y')
      }
    } else {
      destination = {
        x: $(this).data('x'),
        y: $(this).data('y')
      }

      if (current_position === undefined) {
        alert('Choose a piece!')
      } else {
        $.post('/move',
          {
            cur_x: current_position.x,
            cur_y: current_position.y,
            dst_x: destination.x,
            dst_y: destination.y
          },
          function (data, status) {
            $('body').html(data);
            bind_events();
          }
        )
      }
    }
  });
}
