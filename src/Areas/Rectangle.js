import React, { useState } from 'react';
import { Link } from "react-router-dom";

function Rectangle() {
  const [length, setLength] = useState("");
  const [area, setArea] = useState("");
  const [width, setWidth] = useState("");
  const [solution, setSolution] = useState("");

  function handleArea(input) {
    setArea(input.target.value);
  }

  function handleWidth(input) {
    setWidth(input.target.value);
  }

  function handleLength(input) {
    setLength(input.target.value);
  }

  async function handleSubmit(event) {
    event.preventDefault();

    const configs = {
      method: "POST",
      mode: "cors",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        area: area,
        length: length,
        width: width
      })
    }
    fetch("https://eng-calc.herokuapp.com/rectangle", configs).then(response =>
      response.json()
    ).then(solution => setSolution(solution))
  }

  return (
    <form onSubmit={handleSubmit}>
      <p> Rectangular area </p>
      <input
        type="text"
        id="area"
        placeholder="area"
        value={area}
        onChange={handleArea}
      />
      <br/>
      <input
        type="text"
        id="length"
        placeholder="length"
        value={length}
        onChange={handleLength}
      />
      <br/>
      <input
        type="text"
        id="width"
        placeholder="width"
        value={width}
        onChange={handleWidth}
      />
      <button type="submit">Calculate</button>
      <p>{solution}</p>
      <Link to="/Spring">Spring Area</Link>
    </form>
  );
}

export default Rectangle;
