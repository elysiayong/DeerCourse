import React, { useState } from "react";
import { SearchBar } from "./components/SearchBar";
import { ContentCenter } from "./components/StyledComponents";
import utmLogo from "./assets/utm-logo.png";

export const Home = () => {
  // States managing searchbar and results
  const [code, setCode] = useState("");
  const [level, setLevel] = useState("");
  const [duration, setDuration] = useState("");
  const [redirect, setRedirect] = useState(false);
  const states = {
    code,
    setCode,
    level,
    setLevel,
    duration,
    setDuration,
    redirect,
    setRedirect,
  };
  return (
    <ContentCenter>
      <h1 className="main-title"> WELCOME TO DEERCOURSE 🦌</h1>
      <h2 className="main-sub">
        a Course Review Archive by Students at the University of Toronto
        Mississauga
      </h2>
      <br></br>
      <SearchBar showFilter={false} collapsible={false} {...states} />
      <img
        src={utmLogo}
        style={{ position: "absolute", bottom: 25, right: 25, width: 150 }}
        alt="UTM Logo"
      />
    </ContentCenter>
  );
};
