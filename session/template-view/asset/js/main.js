// js 파일로부터 fetchGET, fetchPOST 두 함수 가져옴.
import { fetchGET, fetchPOST } from "./dataFetching.js";

// 서버주소
const SERVER_HOST =
  "https://asia-northeast3-likelion-js-practice.cloudfunctions.net/api";

const NAME = "이상민";

// 쿼리스트링 방식으로 실습진행

// profile데이터가 담긴 
async function getProfileData(name) {
  const path = "/member"    // end point ; 사용자 정보 조회

  // 동기 - 비동기 ; js는 비동기언어다. 그래서 위 줄 코드가 실행되면서 아래코드 실행됨.(위 줄코드가 오래걸리더라도 기다리지 않고 아래코드 실행...) 
  // await를 쓰면 해당줄코드가 다 실행되고 난 후에 아래 줄 코드 실행됨. async는 await를 쓰기 위해 필요함. (그냥 문법이라 외우자.) 

  // fetchGET 함수는 어떤 호스팅서버인지, end point에 어떤식으로 접근하는지, 어떤 객체인지에 따라(매개변수 입력값에 따라) 서버는 각기 다른 데이터를 제공한다. 
  // 프론트엔드는 서버에 요청해서 받은 데이터를 추리고 가공해서 사용자들한테 보여주는 것.

  // fetchGET 함수로 get방식으로 정보 가져옴. ; 근데 path에 "/member"가 들어가니까 사용자정보조회, 즉 원하는 객체정보를 가져온다.
  // 추가로 이 res변수는 getProfileData(name) 함수 내에서만 존재한다.
  const res = await fetchGET(SERVER_HOST, path, {name: name})

  // 변수 res에 담긴 객체에서 키로 원하는 값에 접근해 변수에 저장. 
  // 참고로 해보니까 다음과 같은 접근도 가능하다. 근데 점(.)으로 접근하는 것이 편해서 앞으로 애용할 듯. const myName = res['data']['profile']['name']  
  const myName = res.data.profile.name
  const myMbti = res.data.profile.mbti
  const myGithub = res.data.profile.github

  // 팁) 더블클릭 + 알트 d = 같은 단어 동시에 바꿀 수 있음.

  //DOM으로 html변경
  document.querySelector('.name').innerHTML = myName;
  document.querySelector('.mbti').innerHTML = myMbti;
  document.querySelector('.github').innerHTML = myGithub;
}

// 익명 메세지
async function getFootprint(name) {
  const path = "/footprint"     //footprint조회
  const res = await fetchGET(SERVER_HOST, path, {name: name})

  const messages = res.data.messages

  for(let i =0; i < messages.length; i++) {
    // footprint에 쌓이는 메시지도 인덱스값을 가진다.
    const messageFormat = `
    <div class="board-row">
    ${messages[i]}
    </div>
    `
    // = 으로 그냥 변수에 할당했다면 마지막 메시지만 보여질 것.
    // 그래서 for문과 += 으로 하나씩 추가해준다.
    document.querySelector('.board').innerHTML += messageFormat
  };
}

async function sendFootprint() {
  const path = '/footprint'
  // request body의 형태인 객체형태로 서버에 전달하기 위해.
  const messageObj = {
    content: document.querySelector('.message-content').value,
    receiverName: document.querySelector('.message-sender').value,
  }

  const res = await fetchPOST(SERVER_HOST, path, messageObj);
  // === ; 타입까지 같을 때 사용.
  // 확인차 작성
  if (res.status === 200) {
    alert("메세지를 성공적으로 전송하였습니다.")
  }
}

// 랜더링된 후에 수행할 코드를 묶어 놓은 것 ; window.onload = function () {} 형태로 (암기.)
// 이걸 안쓴다면 랜더링되기도 전에 실행되어 오류가 뜰 수 있다.
window.onload = function () {
  const sendButton = document.querySelector(".send-btn");
  sendButton.addEventListener("click", () => {
    sendFootprint();
  });
  sendButton.addEventListener('click', sendFootprint)
  document.querySelector('.major').innerHTML = "Major: Nursing";
  document.querySelector('.major').style.color = 'coral';
  document.querySelector('.insta').innerHTML = "IG: None";

  getProfileData(NAME);
  getFootprint(NAME);
};

