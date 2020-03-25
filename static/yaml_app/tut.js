var toggler = document.getElementsByClassName("caret");
var i;

for (i = 0; i < toggler.length; i++) {
  toggler[i].addEventListener("click", function() {
    this.parentElement.querySelector(".nested").classList.toggle("active");
    this.classList.toggle("caret-down");
  });
}

function expand_tree() {
  base_toggler = toggler[0].classList.length
  console.log("Base toggler length: " + base_toggler);

  for (i = 0; i < toggler.length; i++) {
    console.log(i + ". toggler length (before)" + toggler[i].classList.length);
    if(toggler[i].classList.length == base_toggler){
      toggler[i].parentElement.querySelector(".nested").classList.toggle("active");
      toggler[i].classList.toggle("caret-down");
    }
    console.log(i + ". toggler length (after)" + toggler[i].classList.length);
  }
}
