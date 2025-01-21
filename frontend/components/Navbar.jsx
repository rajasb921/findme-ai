import React from 'react';

const Navbar = () => {
    return (
        <nav>
            <ul>
                <li>
                    <a href="/" >Home</a>
                </li>
                <li>
                    <a href="/account" >Account</a>
                </li>
                <li>
                    <a href="/images">View Uploads</a>
                </li>
            </ul>
        </nav>
    );
};


export default Navbar;