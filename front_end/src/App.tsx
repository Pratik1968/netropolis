import { useEffect, useState } from 'react'
import './App.css'
import axios from 'axios';

function App() {
  const [test,setTest]= useState("")
  const [test2,setTest2] = useState("")
useEffect(()=>{
axios("/api/fetch").then((res)=>setTest(res.data)).catch(err=>console.log(err))
axios("/api/test").then((res)=>setTest2(res.data))

},[])
  return (
    <>
<p>pratik won</p>
<p>{test}</p>
<p>{test2}</p>
    </>
  )
}

export default App
