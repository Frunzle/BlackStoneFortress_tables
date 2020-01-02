{% extends "layout.html" %}

{%block heading%}
    This is the index page
{% endblock %}

{% block maintext %}
    <form action="{{ url_for('firstpage') }}" method="post">
        <input type="text" name="name" placeholder="Enter name here">
        <button>Submit</button>
    </form>

    <form action="{{ url_for('secondpage') }}" method="post">
        <input type="text" name="note" placeholder="Enter note here">
        <button>Add note to second page</button>
    </form>
{% endblock %}