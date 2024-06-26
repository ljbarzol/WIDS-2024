import React from 'react'
import Logo from '../assets/logo.jpg';

export default function Header() {
  return (
    <div className='flex justify-between px-3 py-6 bg-[#3C5B6F] items-center'>
        <div>
            <p>Logo</p>
            <img src="." alt="" />
        </div>
        <div className='flex text-white'>
            <a className='px-6' href='#'> Home</a>
            <a className='px-6' href='#'> Contacto</a>
        </div>
    </div>
  )
}
