// document.getElementById("btn").addEventListener("click", 
function exam () {
  var random_date, random_number_of_days, start_date;

  const courses = ["DS", "CE", "DB", "SE", "CD", "FDB"];

  for (let i = 0; i <= courses.length; i++) {
    start_date = "2022-1-   ";
    random_number_of_days = Math.random() * 30;
    random_date = start_date + random_number_of_days;
    // my_dict[i] = random_date;

    document.createElement("p").innerHTML = random_date + courses[i]+ "<br>";

    console.log(random-date, courses[i]);
    

  }
  }

exam()
