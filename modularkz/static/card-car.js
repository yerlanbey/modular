
const Cards = ((() => {

  window.addEventListener('DOMContentLoaded', () => {setTimeout(init,1)}, true);

  function init(e)
  {
    if(document.querySelector(".cardsz"))
    {
      let cards = document.querySelector(".cardsz");
      cards.addEventListener('click', clicked, false);
      document.querySelectorAll(".cardsz .cardz")[1].click();
    }
  }


  function clicked(e)
  {
    let card = e.target;
    if(card.getAttribute("data-card")){rearrange(card.getAttribute("data-card"));}
  }


  function rearrange(card)
  {
    let cards = document.querySelectorAll(".cardsz .cardz");
    for(let n = 0; n < cards.length; n++)
    {
      cards[n].classList.remove("cardz--left");
      cards[n].classList.remove("cardz--center");
      cards[n].classList.remove("cardz--right");
    }
    cards[card].classList.add("cardz--center");
    if(card == 0)
    {
      cards[2].classList.add("cardz--left");
      cards[1].classList.add("cardz--right");
    }
    if(card == 1)
    {
      cards[0].classList.add("cardz--left");
      cards[2].classList.add("cardz--right");
    }
    if(card == 2)
    {
      cards[1].classList.add("cardz--left");
      cards[0].classList.add("cardz--right");
    }
  }

  return {
    init
  }
})());