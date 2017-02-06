$(document).ready(bind_events);

function bind_events() {
  var current_position;
  var destination;
  var $selected_piece;

  var $black_squares = $('tr:nth-child(odd) td:nth-child(even), tr:nth-child(even) td:nth-child(odd)');
  $black_squares.click(function () {
    var found_piece_on_the_square = $(this).find('.board__piece').length;
    if (found_piece_on_the_square) {
      $selected_piece = $(this).find('.board__piece').first();
      $('.board__square').removeClass('board__square--selected');
      $(this).addClass('board__square--selected');

      current_position = {
        x: $(this).data('x'),
        y: $(this).data('y'),
        offset_left: $(this).offset().left,
        offset_top: $(this).offset().top
      }
    } else if (current_position === undefined) {
      alert('Please choose a piece first.')
    } else {
      destination = {
        x: $(this).data('x'),
        y: $(this).data('y'),
        offset_left: $(this).offset().left,
        offset_top: $(this).offset().top
      }

      var translate_x = destination.offset_left - current_position.offset_left;
      var translate_y = destination.offset_top - current_position.offset_top;

      $selected_piece.css({
        transform: 'translate(' + translate_x + 'px, ' + translate_y + 'px)',
        transition: 'transform .3s'
      });

      var pieces = pieces_on_board();

      $.post('/move',
        {
          cur_x: current_position.x,
          cur_y: current_position.y,
          dst_x: destination.x,
          dst_y: destination.y,
          pieces: pieces,
          pieces_count: pieces.length,
          board_size: $('tr').length,
          last_move: GameConfig.last_move
        },
        function (data, status) {
          setTimeout(function () {
            $('body').html(data);
            bind_events();
          }, 300);
        }
      );
    }
  });
}

function pieces_on_board() {
  var board_state = [];

  $('.board__piece').each(function () {
    var color;
    if ($(this).hasClass('board__piece--dark')) {
      color = 'DarkPiece';
    }
    if ($(this).hasClass('board__piece--light')) {
      color = 'LightPiece';
    }

    board_state.push({
      x: $(this).parent().data('x'),
      y: $(this).parent().data('y'),
      color: color,
      king: $(this).hasClass('board__piece--king')
    });
  });

  return board_state;
}
