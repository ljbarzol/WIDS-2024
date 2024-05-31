import React from 'react';

export default function Footer() {
  return (
    <footer className="bg-gray-800 text-white py-8 ">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row justify-between">
          <div className="mb-6 md:mb-0">
            <h5 className="font-bold mb-4">Contact Us</h5>
            <ul>
              <li>Email: contact@hackathon.com</li>
              <li>Phone: +123 456 7890</li>
              <li>
                <a href="https://www.facebook.com" className="text-blue-400">Facebook</a>
              </li>
              <li>
                <a href="https://www.twitter.com" className="text-blue-400">Twitter</a>
              </li>
            </ul>
          </div>
          <div className="mb-6 md:mb-0">
            <h5 className="font-bold mb-4">Useful Links</h5>
            <ul>
              <li><a href="#schedule" className="text-blue-400">Schedule</a></li>
              <li><a href="#rules" className="text-blue-400">Rules</a></li>
              <li><a href="#faq" className="text-blue-400">FAQ</a></li>
              <li><a href="#resources" className="text-blue-400">Resources</a></li>
            </ul>
          </div>
          <div className="mb-6 md:mb-0">
            <h5 className="font-bold mb-4">Sponsors</h5>
            <ul>
              <li><a href="https://www.sponsor1.com" className="text-blue-400">Sponsor 1</a></li>
              <li><a href="https://www.sponsor2.com" className="text-blue-400">Sponsor 2</a></li>
            </ul>
          </div>
          <div>
            <h5 className="font-bold mb-4">Legal</h5>
            <ul>
              <li><a href="#privacy-policy" className="text-blue-400">Privacy Policy</a></li>
              <li><a href="#terms-of-service" className="text-blue-400">Terms of Service</a></li>
            </ul>
          </div>
        </div>
        <div className="mt-8 text-center">
          <p>&copy; 2024 Hackathon. All rights reserved.</p>
        </div>
      </div>
    </footer>
  );
}
