// Add event listener to the table rows
document.addEventListener("DOMContentLoaded", function() {
  const tableRows = document.querySelectorAll("tr");
  tableRows.forEach(function(row) {
    row.addEventListener("click", function() {
      console.log("Row clicked!");
    });
  });
});

// Add event listener to the list items
document.addEventListener("DOMContentLoaded", function() {
  const listItems = document.querySelectorAll("li");
  listItems.forEach(function(item) {
    item.addEventListener("click", function() {
      console.log("List item clicked!");
    });
  });
});

// Add some JavaScript code to handle the employee details page
document.addEventListener("DOMContentLoaded", function() {
  const employeeDetails = document.querySelector(".employee-details");
  if (employeeDetails) {
    const attendanceList = employeeDetails.querySelector(".attendance-list");
    attendanceList.addEventListener("click", function(event) {
      if (event.target.tagName === "LI") {
        console.log("Attendance item clicked!");
      }
    });
  }
});