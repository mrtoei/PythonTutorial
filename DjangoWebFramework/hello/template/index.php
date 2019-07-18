<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Django Tutorial</title>
</head>
<body>
    <h1>Hello World</h1>
    <h3>{{ name }}</h3>
    <h3>Age : {{ age }} years old</h3>
    {% if age == 15 %} เด็กน้อย
    {% elif age == 30 %} ใหญ่แล้ววว
    {% else  %} จักแหล่วว
    {% endif  %} 

    <p>
        {% for result in food  %} 
        {{result}}
       
    </p> {% endfor  %} 
    <!-- <h3>food : {{ food }} </h3> -->
</body>
</html>