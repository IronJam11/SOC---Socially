'use client'
import React from "react";
export default function Home()
{
    return(
        <>
        <button onClick={()=>window.location.href = "/home/login"}> Login </button>   <br/>
        <button onClick={()=> window.location.href = "/home/register"}> Register</button>
        </>
    )
}