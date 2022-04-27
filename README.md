<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>API</title>
    <style type="text/css">
        .api {
            background: wheat;
            font-size: 15px;
            padding: 10px 20px;
        }
        .code {
            background: #c9c9c9;
            padding: 10px 20px;
        }
    </style>
</head>
<body>
<h1>Список доступных API</h1>
<h2>Доходы</h2>
<p>Список всех источников дохода. Доступные методы (GET, POST)</p>
<pre class="api">/api/sources/</pre>
<p>Чтобы изменить/удалить источник дохода под id = pk. Доступные методы (GET, PUT, DELETE, OPTIONS)</p>
<pre class="api">/api/sources/< id >/</pre>
<p>Чтобы посмотреть/создать доход. Доступные методы (GET, POST)</p>
<pre class="api">/api/incomes/</pre>
<p>Структура пост запроса для сохранения дохода должны примерно быть такой:</p>
<pre class="code">
    {
        "created": "2022-04-25",
        "amount": 100,
        "category": 1
    }
</pre>
<h2>Расходы</h2>
<p>Чтобы посмотреть список всех категорий с расходами или создать новую категорию. Доступные методы (GET, POST)</p>
<pre class="api">/api/categories/</pre>
<p>Чтобы изменить/удалить категорию расходов c требуемой id. Доступные методы (GET, PUT, DELETE, OPTIONS)</p>
<pre class="api">/api/categories/< id >/</pre>
<p>Чтобы добавить сразу несколько затрат или посмотреть все затраты. Доступные методы (GET, POST)</p>
<pre class="api">/api/expenses/</pre>
<p>Структура пост запроса для сохранения расходов должны примерно быть такой:</p>
<pre class="code">
    {
      "data": [
        {
          "created": "2022-04-25",
          "amount": 1000,
          "currency": "BYN",
          "category": 1
        },
        {
          "created": "2022-04-25",
          "amount": 100,
          "currency": "BYN",
          "category": 2
        },
        {
          "created": "2022-04-25",
          "amount": 290,
          "currency": "BYN",
          "category": 3
        }
      ]
    }
</pre>

<p>Чтобы посмотреть/сохранить/изменить дату дохода. Доступные методы (GET, POST)</p>
<pre class="api">/api/set-day/</pre>
<p>Структура пост запроса для сохранения/изменения дня необходимого дохода примерно быть такой:</p>
<pre class="code">
    {
        "salary_day": "20",
        "source": 1  # Здесь id источника дохода
    }
</pre>
<p>Чтобы посмотреть/сохранить/изменить относительную величину. Доступные методы (GET, POST)</p>
<pre class="api">/api/relativity/</pre>
<p>Структура пост запроса для сохранения/изменения дня необходимого дохода примерно быть такой:</p>
<pre class="code">
    {
        "name": "Пиво",
        "value": "л",
        "amount: 3.5
    }
</pre>
</body>
</html>