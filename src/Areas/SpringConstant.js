import React, { useState } from 'react';
import '../App.css';

function SpringConstant() {
  const [sc, setSC] = useState("");
  const [distE, setDistE] = useState("");
  const [sprE, setSprE] = useState("");
  const [force, setForce] = useState("");
  const [solution, setSolution] = useState("");

  function handleSC(input) {
    setSC(input.target.value)
  }

  function handleForce(input) {
    setForce(input.target.value)
  }

  function handleSprE(input) {
    setSprE(input.target.value)
  }

  function handleDistE(input) {
    setDistE(input.target.value)
  }

  async function handleSubmit(event) {
    event.preventDefault();
    const configs = {
      method: "POST",
      mode: "cors",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        sc: sc,
        force: force,
        distE: distE,
        sprE: sprE
      })
    }
    fetch("https://eng-calc.herokuapp.com/sc", configs).then(response =>
      response.json()
    ).then(solution => setSolution(solution))
  }

  return (
    <form onSubmit={handleSubmit}>
      <p> Spring Constant </p>
      <input
        type="text"
        id="area"
        placeholder="Spring Constant"
        value={sc}
        onChange={handleSC}
      />
      <br/>
      <input
        type="text"
        id="length"
        placeholder="Force"
        value={force}
        onChange={handleForce}
      />
      <br/>
      <input
        type="text"
        id="width"
        placeholder="Distance E"
        value={distE}
        onChange={handleDistE}
      />
      <br/>
      <input
        type="text"
        id="width"
        placeholder="Spring E"
        value={sprE}
        onChange={handleSprE}
      />
      <button type="submit">Calculate</button>
      <p>{solution}</p>
    </form>
  );
}

export default SpringConstant;
