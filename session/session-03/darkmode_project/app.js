// js는 오픈라이브서버로 보기 힘들고 콘솔로그를 통해 확인가능.

// querySelector(selectors) : 로 불러오는 것이 더 구체적

// const checkbox = document.getElementById("checkbox")
const checkbox = document.querySelector('.checkbox');
console.log(checkbox);

// // 이벤트는 사용자의 반응
checkbox.addEventListener('click', click);

// classList 는 js가 css를 통제할 수 있게 해줌.
// 
function click() {
    if (document.body.classList.contains("dark")) {
        document.body.classList.remove('dark');
        console.log('convert into Light Mode')
    } else {
        document.body.classList.add('dark');
        console.log('convert into Dark Mode')
    }
}

// toggle 형식 ; 원래 js가 가지고 있는 기능임.
// function toggleClick() {
//     document.body.classList.toggle('dark');
//     // working 하면서 숫자올라감.
//     console.log('Working!')
// }