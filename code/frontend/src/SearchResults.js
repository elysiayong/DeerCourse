import React, { useState } from "react";
import { SearchBar } from "./components/SearchBar";
import { ResultInfo } from "./components/ResultInfo";
import { Content } from "./components/StyledComponents";

export const SearchResults = (props) => {
  // States managing searchbar and results
  const [code, setCode] = useState(props.code ? props.code : "");
  const [level, setLevel] = useState(props.level ? props.level : "");
  const [duration, setDuration] = useState(
    props.duration ? props.duration : ""
  );
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
    <Content>
      <SearchBar showFilter={true} collapsible={false} {...states} />
      <ResultInfo
        code={props.code}
        level={props.level}
        duration={props.duration}
      />
    </Content>
  );
};
