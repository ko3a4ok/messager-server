<h2>
    Server info for ${request.host}
</h2>

<p>
    The URL you called: ${session['name']}
</p>

<p>
    The name you set: ${c.name}
</p>

<p>The WSGI environ:<br />
<pre>${c.pretty_environ}</pre>
</p>

<h1>${c.name or "FUCK MMEEE"}</h1>