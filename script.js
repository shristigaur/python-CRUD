// function styleChange() {
//     const change = document.getElementById("pic");
//     change.style.color = "Brown";
//     alert("button is clicked");
// }

// let pattern = document.getElementsByTagName("p");
// for (let i=0; i<pattern.length; i++){
//     pattern[i].style.fontStyle = "italic";

// }

// function under(){
//     let step = document.getElementsByClassName("highlight");
//    for(let i=0; i<step.length; i++){
//        step[i].style.textDecoration = "underline";
//     }
// }
// let beck = document.querySelector("button");
// beck.textContent = "now change this position";

// let set = document.querySelectorAll("button");
// for (let i=0; i<set.length; i++){
//     set[i].style.display="block";
//     set[i].style.padding="10px";
//     set[i].style.color="purple";
//     set[i].style.borderRadius="5%";
// }

// let lane = document.querySelector(".box span");
// lane.textContent = "change my sheet fact";

// let deck = document.getElementById("ret");
// deck.textContent = "i am there";

// let safe = document.getElementById("case");
// safe.innerHTML = "please enter your no. here";

    
// function face(){
//     let date = document.getElementById("flirt");
//     date.classList.add("ding");
//     date.classList.remove("king");
//     alert("button is clicked");
// }

// function lent(){
//     car = document.getElementById("wet");
//     car.classList.toggle("log");
//     alert("button is clicked");
// }

// function fat(){
//     define = document.getElementById("frog");
//     define.setAttribute("src", "worst.jpg");
//     alert("button is clicked");
// }

// let clear= document.getElementById("yap");
// clear.getAttribute("href");
// console.log(clear)

// let explain=document.createElement("p");
// explain.textContent="You can log it, count clicks, or validate the link before allowing the user to go there.";
// let routine=document.getElementById("heck");
// routine.append(explain);

// let tray=document.createElement("li")
// tray.textContent = "ITEM3";
// let finger = document.getElementById("prank");
// finger.append(tray);

// let vapire=document.createElement("button");
// vapire.textContent="hide your heart for your parents";
// let server=document.getElementById("sweet");
// let paper=document.getElementById("just");
// server.insertBefore(vapire, paper);

// let dog=document.getElementById("page");
// dog.style.backgroundColor="pink";
// let given=document.getElementById("land");
// dog.removeChild(given);

// let energy=document.getElementById("peter");
// energy.addEventListener("click", function() {
// energy.style.backgroundColor = "orange";
// });

// let pookie=document.getElementById("floor");
// pookie.removeEventListener("click", function() {
// pookie.style.backgroundColor = "orange";
// });

// let label=document.getElementById("flower");
// label.addEventListener("mouseover", function() {
// this.style.background = "orange";
// });


// let linker=document.getElementById("cow");
// linker.addEventListener("keydown", function(event) {
//     if (event.key === "Enter") {
//         alert("you pressed enter!");
//     }
// });

// let vet=document.getElementById("hader");
// vet.addEventListener("change", function(){
//     alert("you are selected: " +this.value);
// });

// let fever=document.getElementById("beat");
// fever.addEventListener("submit", function(toller){
//     toller.preventDefault();
//     alert("your form is submited");
// });

// let corprate=document.getElementById("poddle");
// corprate.addEventListener("dblclick", function(){
//     this.style.backgroundColor = "purple";
// });

// let rockland=document.getElementById("makup");
// rockland.addEventListener("mouseover", function(){
//     this.style.fontSize = "40px";
// });

// rockland.addEventListener("mouseout", function(){
//     this.style.fontSize= "10px";
// });

// function clock(){
//     let clap=document.getElementById("joker");
//     clap.style.display= "none";
// }

// // after this i am doing practise in this js for learning more

// let trex = document.getElementById("possion");
// trex.textContent = "Welcome to my heart";

// function weapon(){
//    let demon=document.getElementById("hockey");
//    demon.setAttribute("src", "collage.jpeg");
// }

// function xtree(){
//     let peagon=document.getElementById("bee");
//     peagon.classList.toggle('grapes');
// }

// let yummy=document.createElement("li");
// yummy.textContent = "ITEM3: PANf";
// let dipper=document.getElementById("happen");
// dipper.append(yummy);

// let settlement=document.getElementById("pikle");
// settlement.addEventListener("mousemove", function(){
//     this.style.display = "none";
// });

// let wood=document.getElementById("wool").value;
// console.log(wood);

// let patel=document.getElementById("jeap");
// patel.addEventListener("click", function(){
//     this.style.backgroundColor = "blue";
// })

// var huke = document.querySelector('h4');
// huke.innerHTML="h1 element's id value:";

// function yes(){
//     let flok=document.getElementById("wool").value;
//     alert("hello! " +flok);
// }

// function keepgo(){
    
// }
//   let g = document.querySelector("#pagal");

//   g.addEventListener("click", function(e) {
//     e.preventDefault(); // stops the link from opening
//     alert("Link clicked, but not redirected.");
//   });

// let elephat=document.getElementById("met");
// elephat.innerText='<strong>hello! i am here</strong>';
// elephat.innerHTML = `
//     <ul>
//         <li>Item 1</li>
//         <li>Item 2</li>
//     </ul>
// `;
// elephat.innerText = 'Line 1\nLine 2\nLine 3';

// console.log(elephant)

let myButton = document.getElementById("flow");
let ma=document.getElementById("ma");
myButton.addEventListener("click", function() {
    if (ma.paused){
        ma.play();
        myButton.textContent = "Pause";
    }
    else{
        ma.pause();
        myButton.textContent = "Play";
    }
})

let temp=document.createElement("button");
temp.textContent="click me";
temp.addEventListener("keydown", function(){
    temp.style.backgroundColor="red";
    temp.textContent="i am clicked";
});
document.body.append(temp);
let jet=document.getquerySelector("#join");
jet.addEventListener("submit", function(events){
    events.preventDefault();
    console.log("form submitted");
})

  const btn1 = document.getElementById('btn1');
  const btn2 = document.getElementById('btn2');

  const answer1 = document.getElementById('answer1');
  const answer2 = document.getElementById('answer2');

  // 2. Get the icons inside the buttons (so we can change + to -)
  const icon1 = btn1.querySelector('i');
  const icon2 = btn2.querySelector('i');

  // ----- helper function to toggle one answer -----
  function toggleAnswer(button, answerBox, icon) {
    // check if answer is currently hidden
    const isHidden = !answerBox.classList.contains('show');

    if (isHidden) {
      // show answer
      answerBox.classList.add('show');
      // change icon to minus
      icon.className = 'fas fa-minus';
      // optional: change button background (just for fun)
      button.style.background = '#cbe0f5';
    } else {
      // hide answer
      answerBox.classList.remove('show');
      // change icon back to plus
      icon.className = 'fas fa-plus';
      button.style.background = '';
    }
  }

  // ----- attach click events -----

  // For question 1
  btn1.addEventListener('click', function() {
    toggleAnswer(btn1, answer1, icon1);
  });

  // For question 2
  btn2.addEventListener('click', function() {
    toggleAnswer(btn2, answer2, icon2);
  });

  // (optional) a tiny extra: click on the question text also works?
  // but we keep it simple – only the button.
  console.log('✅ Ready! Click the + buttons.');
  
