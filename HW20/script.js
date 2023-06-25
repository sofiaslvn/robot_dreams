document.addEventListener("DOMContentLoaded", function () {

  var friendsCount = Math.floor(Math.random() * 100);


  var friendsCountElement = document.createElement("span");
  friendsCountElement.id = "friendsCount";
  friendsCountElement.textContent = friendsCount + " друзів";


  var addButton = document.getElementById("addFriendButton");
  addButton.parentNode.insertBefore(friendsCountElement, addButton);


  addButton.addEventListener("click", function () {
    if (!addButton.disabled) {
      friendsCount++;
      friendsCountElement.textContent = friendsCount + " друзів";
      addButton.disabled = true;
      addButton.textContent = "Очікується підтвердження";
    }
  });
});


function getContrastColor(color) {
  var r = parseInt(color.slice(1, 3), 16);
  var g = parseInt(color.slice(3, 5), 16);
  var b = parseInt(color.slice(5, 7), 16);
  var yiq = (r * 299 + g * 587 + b * 114) / 1000;
  return yiq >= 128 ? "#000000" : "#ffffff";
}


var messageButtonState = 0;

function changeMessageButtonColor() {
  var messageButton = document.getElementById("messageButton");

  if (messageButtonState === 0) {

    messageButton.style.backgroundColor = "red";
    messageButton.style.color = getContrastColor("red");
    messageButtonState = 1;
  } else {

    messageButton.style.backgroundColor = "";
    messageButton.style.color = "";
    messageButtonState = 0;
  }
}


function submitHomework() {
  var table = document.querySelector(".table");


  var newRow = document.createElement("tr");


  var newCell = document.createElement("td");
  var homeworkText = "Здане нове дз";
  newCell.textContent = homeworkText;


  newRow.appendChild(newCell);


  table.appendChild(newRow);
}


document.getElementById("addFriendButton").addEventListener("click", function () {
  addFriend();
});


document.getElementById("messageButton").addEventListener("click", function () {
  changeMessageButtonColor();
});


document.getElementById("submitHomeworkButton").addEventListener("click", function () {
  submitHomework();
});


var initialFriendCount = getRandomNumber(0, 100);
updateFriendCount(initialFriendCount);