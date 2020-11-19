$('#play-video').on('click', function(e){
  e.preventDefault();
  $('#video-overlay').addClass('open');
  $("#video-overlay").append('<iframe width="560" height="315" src="https://www.youtube.com/embed/ngElkyQ6Rhs" frameborder="0" allowfullscreen></iframe>');
});

$('.video-overlay, .video-overlay-close').on('click', function(e){
  e.preventDefault();
  close_video();
});

$(document).keyup(function(e){
  if(e.keyCode === 27) { close_video(); }
});

function close_video() {
  $('.video-overlay.open').removeClass('open').find('iframe').remove();
};



/*
  @method Cards
  @description this is for label based radio navigation to change the labels style to 'active'
 */
const Cards = ((() => {
  /*
   * @description dom loaded event listener
   */
  window.addEventListener('DOMContentLoaded', () => {setTimeout(init,1)}, true);

  /*
   * @method init
   * @parameter e {event}
   * @description initiates event listeners on all cards
   */
  function init(e)
  {
    if(document.querySelector(".cardsq"))
    {
      let cards = document.querySelector(".cardsq");
      cards.addEventListener('click', clicked, false);
      document.querySelectorAll(".cardsq .cardq")[1].click();
    }
  }

  /*
   * @method clicked
   * @parameter e {event}
   * @description this is the callback from the assigned event listener binding
   */
  function clicked(e)
  {
    let card = e.target;
    if(card.getAttribute("data-card")){rearrange(card.getAttribute("data-card"));}
  }

  /*
   * @method rearrange
   * @parameter card {object}
   * @description this is the callback from the assigned event listener binding
   */
  function rearrange(card)
  {
    let cards = document.querySelectorAll(".cardsq .cardq");
    for(let n = 0; n < cards.length; n++)
    {
      cards[n].classList.remove("cardq--left");
      cards[n].classList.remove("cardq--center");
      cards[n].classList.remove("cardq--right");
    }
    cards[card].classList.add("cardq--center");
    if(card == 0)
    {
      cards[2].classList.add("cardq--left");
      cards[1].classList.add("cardq--right");
    }
    if(card == 1)
    {
      cards[0].classList.add("cardq--left");
      cards[2].classList.add("cardq--right");
    }
    if(card == 2)
    {
      cards[1].classList.add("cardq--left");
      cards[0].classList.add("cardq--right");
    }
  }

  return {
    init
  }
})());