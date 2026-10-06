// // game=document.body
// // const idlearn=document.getElementById("call");
// // // idlearn.textContent="my name is expension there is now any learning of a copy paste work";
// // idlearn.innerHTML="smart <span> expensive for learning</span>";
// // console.log(idlearn);
// // game.append(idlearn)
// // const expenseForm =document.getElementById("exform");
// // const expenseName =document.getElementById("expenseName");
// // const expenseAmount =document.getElementById("expenseAmount");
// // const expenseCategory =document.getElementById("expenseCategory");
// // console.log(expenseForm);
// // console.log(expenseName);
// // console.log(expenseAmount);
// // console.log(expenseCategory);
// // console.log(expenseName.value);
// // console.log(expenseAmount.value);
// // console.log(expenseCategory.value);
// // expenseForm.addEventListener("submit", function(event){
// //     if (name===""){
// //         nameError.textContent="Name is required";
// //         return;
// //     }
// //     event.preventDefault();
// //     console.log("form submitted");
// // });
// // exform.addEventListener("submit", function(event){
// //     event.preventDefault();
// //     const name=expenseName.value.trim();
// //     const amount=expenseAmoutn.value;
// //     const category=expenseCategory.value;
// //     console.log(name);
// //     console.log(amount);
// //     console.log(category);
// // });
// // const nameError=document.getElementById("nameError");
// // const amountError=document.getElementById("amountError");
// // const categoryError=document.getElementById("categoryError");

// const { createElement } = require("react");

// // expenseForm.addEventListener(
// //     "submit",
// //     function (event) {

// //         event.preventDefault();


// //         const name =
// //             expenseName.value.trim();


// //         if (name === "") {

// //             nameError.textContent =
// //                 "Expense name is required.";

// //             return;
// //         }


// //         console.log(name);

// //     }
// // );
// // const female=document.getElementById("call");
// // const pem=female.parentNode;
// // parent.style.backgroundColor = "lightblue";

const pet=document.getElementById("parent");
console.log(pet.lastElementChild);
const ch=document.getElementById("child");
console.log(ch.nextElementSibling);
const g=document.querySelector("button");
console.log(g.previousElementSibling);
console.log(pet.parentElement.parentElement)
console.log(pet.childNodes)
const gift=document.createElement("h1");
gift.textContent="i am the best in the world";
gift.classList.add("mental");
document.body.append(gift)
const met=document.querySelector(".mental");
met.innerHTML="<p>there is a side effect</p>";
met.style.color="red";
const mono=document.getElementById("poki");
const best=document.createElement("button");
const nano=document.createElement("p");
nano.textContent="there is no on are on this page to read any content";
best.textContent="click this page";
best.style.color="red";
poki.append(best, nano);
// const text=document.getElementById("text");
// poki.appendChild(text);

const bottle=document.getElementById("bottle");
const news=document.createElement("p");
news.textContent="this is a new paragraph";
bottle.prepend(news)

// let email= prompt("add email:" );

// if (email.includes("@gmail.com")){
//     console.log("correct")
//     alert("correct")
// }
// else{
//     alert("incorrect")
// }


const sell=document.getElementById("savei");
const updat=document.getElementById("updat");
const result=document.getElementById("result");
const casting=document.getElementById("being");
const there=document.getElementById("there");
sell.addEventListener("click", ()=>{
    const name=casting.value;
    localStorage.setItem("username", name);
    alert("data is successfully saved there")
})
updat.addEventListener("click", ()=>{
    const sname=localStorage.getItem("username");
    there.innerHTML="";
    const li=document.createElement("li");
    li.textContent=`conte name: ${sname}`;
    there.append(li);
    result.textContent=sname;
})
// sessionStorage.setItem("username", "expension");
// const note=sessionStorage.getItem("username");
// console.log(note);
// sessionStorage.removeItem("note");
// sessionStorage.clear()

const till={
    name:"shristi",
    age:22,
    address:"delhi"
};
localStorage.setItem("userinfo", JSON.stringify(till));
const dem=localStorage.getItem("userinfo");
console.log(JSON.parse(dem));

// const user = {
//   name: "Shristi",
//   age: 22,
//   city: "Delhi"
// };

// localStorage.setItem(
//   "user",
//   JSON.stringify(user)
// );
// const storedUser = localStorage.getItem("user");

// const users = JSON.parse(storedUser);

// console.log(users.name);

const input = document.getElementById("todoInput");
const addBtn = document.getElementById("addBtn");
const todoList = document.getElementById("todoList");

// Get existing todos
let todos = JSON.parse(
  localStorage.getItem("todos")
) || [];

// Display existing todos
function displayTodos() {
  todoList.innerHTML = "";

  todos.forEach(function (todo) {
    const li = document.createElement("li");

    li.innerText = todo;

    todoList.append(li);
  });
}

// Add Todo
addBtn.addEventListener("click", function () {
  const task = input.value;

  if (task === "") {
    return;
  }

  // Add to array
  todos.push(task);

  // Save array
  localStorage.setItem(
    "todos",
    JSON.stringify(todos)
  );

  // Display updated todos
  displayTodos();

  input.value = "";
});

// Show todos when page loads
displayTodos();

console.log(window);
// window.alert("hksdjfioerh")
console.log(window.innerWidth)
console.log(location.href)
console.log(location.hostname)
console.log(history)
history.back()
console.log(navigator)
console.log(navigator.language)
if (navigator.online){
    console.log("you are online");
} else{
    console.log("you are not online")
}

// const timer = setTimeout(() => {
//     console.log("Your session is about to expire");
// }, 5000);

// function cancelMessage() {
//     clearTimeout(timer);
// }

const box = document.getElementById("box");
const button = document.getElementById("button");

box.addEventListener("click", () => {
    console.log("Box clicked");
});

button.addEventListener("click", () => {
    console.log("Button clicked");
});



// const products = document.getElementById("products");

// products.addEventListener("click", (event) => {
//     console.log(event.target.textContent);
// });

const items = document.querySelectorAll("#products li");

items.forEach(item => {
    item.addEventListener("click", () => {
        console.log(item.textContent);
    });
});

const grandparen = document.getElementById("grandparen");
const paren = document.getElementById("paren");
const chil = document.getElementById("chil");

grandparen.addEventListener("click", () => {
    console.log("Grandparen");
});

paren.addEventListener("click", () => {
    console.log("Paren");
});

chil.addEventListener("click", () => {
    console.log("Chil");
});

const dis=document.getElementById("dis");
const start=document.getElementById("start");
const stope=document.getElementById("stope");
const reset=document.getElementById("reset");

let s=0;
let t=null;
start.addEventListener("click", ()=>{
    t=setInterval(()=>{
        s++;
        let h=Math.floor(s/3600);
        let m=Math.floor((s%3600)/60);
        let se=s%60;
        dis.textContent=`${h}:${m}:${se}`;
    }, 1000);
})

reset.addEventListener("click", ()=>{
    clearInterval(t);
    s=0;
    dis.textContent="0:0:0";
})

stope.addEventListener("click", ()=>{
    clearInterval(t);
})

const mobile=document.getElementById("mobile");
const laptop=document.getElementById("laptop");
const drop=document.getElementById("drop");
const engine=document.getElementById("engine");
let tgs=null;

mobile.addEventListener("click", ()=>{
    if (tgs){
        clearInterval(tgs);
        tgs=null;
    }
    let tg=Number(engine.value);
    if (isNaN(tg) || tg<=0){
        drop.textContent="please enter valid number"
        return;
    }
     tgs=setInterval(()=>{
        if (tg<=0){
            clearInterval(tgs);
            drop.textContent="time up now you are out of the game be serious";
            return;
        }
        drop.textContent=tg;
        tg--;
    }, 1000)
});

laptop.addEventListener("click", ()=>{
    if (tgs){
        clearInterval(tgs);
        tgs=null;
    }
    clearInterval(tgs);
    drop.textContent="00";
    engine.value="";
    engine.focus();
})

function bite(){
    console.log("hello");
}
function except(fo){
    console.log(fo, "shristi");
}
except(bite)

function beginer(){
    console.log("hello world");
}
function sept(fn){
    fn();
}
sept(beginer)

let pig=[1, 2, 3, 4, 5, 6, 7]
for (let i=0; i<pig.length; i++){
    console.log(pig[i]);
}

let gig=[1, 6, 5, 4, 90, 23, 56]
const big=gig.forEach(i=>{
    return i*2;
})
console.log(big)

let backup=["apple", "mango", "lichi", "grapes", "gavava"]
backup.forEach((i, j)=>{
    console.log(`fruit is there ${i} and its index is there ${j}`);
})

let parrot=["apple", "mango", "chilli"]
parrot.map((i, j)=>{
    console.log(`there is a fruit name are ${i} and its index is ${j}`)
})

let pain=["apple", "mango", "orange", "banana", "able", "cournt"]
let kill=pain.filter((i)=>{
    if (i=>"aeiou".includes(i[0].toLowerCase())){
        return true;
    }
})
console.log(kill)

hate=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
const vine=hate.reduce((s, n)=> s+n, 0)
console.log(vine)

jine=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
const jinne=jine.every((bo)=>{
    return bo%2===0;
})
console.log(jinne)

banner=[[1, 2,], [3, 4, 5], [6, 7, 8]]
console.log(banner.flat());


const hello=document.getElementById("hello");
const mam=document.getElementById("mam");
const shri=document.getElementById("shri");
const shro=document.getElementById("shro");
shri.addEventListener("click", ()=>{
    const name=hello.value;
    localStorage.setItem("username", JSON.stringify(name));
    alert("data is successfully saved there");
})
shro.addEventListener("click", ()=>{
    const sname=localStorage.getItem("username");
    mam.innerHTML="";
    mam.textContent=`content name: ${sname}`;
})

function c(){
    let co=0;
    return function(){
        co++;
    };
}
const fo=c()
fo()
fo()
fo()

for (var i=1; i<=3; i++){
    setTimeout(function(){
        console.log(i);
    }, 1000)
}
console.log(this)

const user={
    name:"shristi",
    greet(){
        console.log(this.name);
    }
};
user.greet();

function s(){
    console.log(this);
}
s();


const namc="shristi"
const cop={...namc}
cop.namc="binn"
console.log(namc)


