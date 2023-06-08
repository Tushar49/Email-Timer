# Email Timer 

Email Timer is a web application that allows users to set timers for their email accounts so they know when they can next use them.

## Purpose

Many online services limit how often you can perform certain actions, like sending emails, to prevent abuse. However, it can be hard to keep track of when these limits reset. Email Timer solves this problem by allowing you to easily set timers for any email account.

Once a timer is started, Email Timer will run it in the background and notify you when it's done so you know you can use that email account again. This ensures you never have to worry about hitting usage limits or having your account suspended due to overuse.

## Features

- Set timers for any email account 
- Choose timer durations from 1 hour up to 1 week
- Receive browser notifications when timers complete
- Responsive design works on both desktop and mobile
- Open source and free to use

## Getting Started

Follow these steps to set up Email Timer locally:

1. Clone the repository:

```git clone https://github.com/Tushar49/Email-Timer
```
 2. Install the required packages:

```pip install -r requirements.txt```

3. Set the environment variables:

```
export FLASK_APP=app.py
export FLASK_ENV=development
```

4. Run the app:

```flask run```

5. Navigate to http://localhost:5000 in your browser

6. Enter the email address you want to set a timer for and select a duration. 

7. Click "Start Timer" to begin the countdown.

8. You will receive a browser notification once the timer is complete.

9. You can now use the email account again!

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

