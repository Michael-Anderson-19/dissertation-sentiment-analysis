import React, { useState, useEffect } from 'react'
import Header from './components/Header';
import Input from './components/Input';
import MainResult from './components/MainResult';
import ResultsList from './components/ResultsList';
import Footer from "./components/Footer";



function App() {

  const [darkMode, setDarkMode ] = useState(false);
  const [error, setError] = useState("");
  const [isLoading, setLoading] = useState(false);
  const [mainPrediction, setMainPrediciton] = useState('')
  const [inputText, setInputText] = useState('');
  const [mainProbability, setMainProbability] = useState('')
  const [tweetPredicitons, setTweetPredicitons] = useState([])
  const [disableButtons, setDisableButtons] = useState(false); 

  //make fetch request
  const  makeRequest = async (URL, data) => {
    const request = await fetch(URL, {
      method : 'post', 
      mode : 'cors', 
      headers : { 'Content-Type':'application/json' },
      body : JSON.stringify(data)
    })
    return await request.json(); 
  }

  //save the dark mode options to local storage
  const persistDarkModeSetting = () => {

  }

  //load the dark mode options from local storage
  const loadDarkModeSetting = () => {

  }

  //load the darkmode options when the app starts 
  useEffect( ()=>{},[])

  //save the darkmode options to local storage when the state changes 
  useEffect( ()=>{},[])

  //clear all state and fiels 
  const clearEverything = () => {
    setInputText("");
    setMainPrediciton("");
    setMainProbability("");
    setTweetPredicitons([]);
    setError("");
    setLoading(false);

  }
 
   //set the state variables from the request response
   const  handleResponse = ({prediction, probability, tweets}) => {

    setMainPrediciton(prediction);
    setMainProbability(probability);
    setTweetPredicitons(tweets);

  }

  
  const handleError = (errorMessage) =>
  {
    setError(errorMessage);
  }

  //make a prediction to the api and handle the response
  const makePredictionRequest = () => {
    const URL = "http://localhost:5000/predict/tweets" 
    const data = {text: inputText};
    clearEverything();
    if(!data.text)
    {
      setError("text field must not be empty when making a request")
      return;
    }
    setLoading(true)
    setDisableButtons(true); 

    makeRequest(URL,data).then( (jsonData) => {
    setLoading(false)
    setInputText(jsonData.keyword)
    setDisableButtons(false); 

    //set error for server errors returned from api
    if(jsonData.status !== 200)
    {
      handleError(`${jsonData.status} ${jsonData.message}`);
      return;              
    }

    handleResponse(jsonData)

  }).catch( e =>  {
      setLoading(false)
      handleError(e.message);
      setDisableButtons(false); 
    });
  
}


  return (
    <div className={"app-container " + (darkMode ? "dark-theme" : "light-theme")} >
      <Header handleThemeChange={setDarkMode}/>
      <div className="content-container">
        <Input textValue={inputText} handleTextInput={setInputText} clearText={clearEverything} makePrediciton={makePredictionRequest} disable={disableButtons}/>
        <MainResult mainPred={mainPrediction} mainProb={mainProbability} isLoading={isLoading} error={error}/>
        <ResultsList tweetPredicitons={tweetPredicitons}/>
      </div>
      <Footer/>
    </div>
  );
}

export default App;