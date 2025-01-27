const transactions = [];
let totalIncome = 0;
let totalExpense = 0;

function updateTotals() {
  totalIncome = transactions
    .filter(transaction => transaction.type === "income")
    .reduce((sum, transaction) => sum + transaction.amount, 0);

  totalExpense = transactions
    .filter(transaction => transaction.type === "expense")
    .reduce((sum, transaction) => sum + transaction.amount, 0);

  const balance = totalIncome - totalExpense;

  document.getElementById("balance").textContent = balance.toFixed(2);
  document.getElementById("totalIncome").textContent = totalIncome.toFixed(2);
  document.getElementById("totalExpense").textContent = totalExpense.toFixed(2);

  drawPieChart();
}

function drawPieChart() {
  const canvas = document.getElementById("pieChart");
  const ctx = canvas.getContext("2d");

  // Clear the canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  const total = totalIncome + totalExpense;

  if (total === 0) {
    ctx.font = "16px Arial";
    ctx.fillStyle = "#000";
    ctx.textAlign = "center";
    ctx.fillText("No Data to Display", canvas.width / 2, canvas.height / 2);
    return;
  }

  const incomeAngle = (totalIncome / total) * 2 * Math.PI;
  const expenseAngle = (totalExpense / total) * 2 * Math.PI;

  // Draw income slice
  ctx.beginPath();
  ctx.moveTo(canvas.width / 2, canvas.height / 2);
  ctx.arc(canvas.width / 2, canvas.height / 2, 150, 0, incomeAngle);
  ctx.fillStyle = "#4CAF50"; // Green
  ctx.fill();

  // Draw expense slice
  ctx.beginPath();
  ctx.moveTo(canvas.width / 2, canvas.height / 2);
  ctx.arc(
    canvas.width / 2,
    canvas.height / 2,
    150,
    incomeAngle,
    incomeAngle + expenseAngle
  );
  ctx.fillStyle = "#F44336"; // Red
  ctx.fill();
}

document.getElementById("transactionForm").addEventListener("submit", event => {
  event.preventDefault();

  const type = document.getElementById("type").value;
  const amount = parseFloat(document.getElementById("amount").value);

  if (isNaN(amount) || amount <= 0) {
    alert("Please enter a valid amount.");
    return;
  }

  transactions.push({ type, amount });
  updateTotals();

  document.getElementById("transactionForm").reset();
});

// Initial rendering
updateTotals();
