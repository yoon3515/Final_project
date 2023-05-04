// 모달 창 열기 함수
function openModal(image, fishName, caughtDate) {
  // 모달 요소 가져오기
  var modal = document.getElementById("myModal");
  // 이미지 요소 가져오기
  var modalImg = document.getElementById("modal-image");
  // 첫 번째 텍스트 요소 가져오기
  var modalText = document.getElementById("modal-text");
  // 두 번째 텍스트 요소 가져오기
  var modalSecondText = document.getElementById("modal-text2");

  // 모달 내용 채우기
  modalImg.src = image;
  modalText.innerHTML = fishName;
  modalSecondText.innerHTML = caughtDate;

  // 모달 열기
  modal.style.display = "block";
}

// 모달 창 닫기 함수
function closeModal() {
  // 모달 요소 가져오기
  var modal = document.getElementById("myModal");

  // 모달 닫기
  modal.style.display = "none";
}

// 배경 클릭 시 모달 닫기
var modal = document.getElementById("myModal");
window.onclick = function(event) {
  if (event.target == modal) {
    closeModal();
  }
}

