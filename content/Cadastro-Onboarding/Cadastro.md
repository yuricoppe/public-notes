---
title: "Cadastro"
description: "Links e trechos sobre simplificar formulários de cadastro e login, incluindo alternativas ao CAPTCHA"
tags:
  - tema/ux
  - tipo/links
---

## Artigos

- **[Web Form Design Patterns: Sign-Up Forms](https://www.smashingmagazine.com/2008/07/web-form-design-patterns-sign-up-forms/)** · Smashing Magazine · 2008
- **[Web Form Design Patterns: Sign-Up Forms, Part 2](https://www.smashingmagazine.com/2008/07/web-form-design-patterns-sign-up-forms-part-2/)** · Smashing Magazine · 2008

---

**[Innovative Techniques To Simplify Sign-Ups And Log-Ins](https://www.smashingmagazine.com/2011/05/innovative-techniques-to-simplify-signups-and-logins/)** · Smashing Magazine · 2011
### Combat Spam by Hiding a Text Field With JavaScript, Instead of Using CAPTCHA

If you get a lot of spam, then putting a CAPTCHA on your form may be necessary. What’s _not_ necessary is making the CAPTCHA an obstacle that turns users away. Traditional CAPTCHAs that ask users to retype distorted letters have been proven to hurt conversion rates. With the extra hassle they force on users, it’s no wonder.

- [CAPTCHA’s Effect on Conversion Rates](https://www.seomoz.org/blog/captchas-affect-on-conversion-rates)
- [F**k CAPTCHA](https://www.90percentofeverything.com/2011/03/25/fk-captcha/)

A simpler approach that won’t lower your conversion rate is to use a hidden and required text field generated with client-side Javascript. Spambots can’t fill in the field because they can’t interact with objects in client-side JavaScript; only users can. This method is simpler and less intrusive and so will reduce spam without hurting your conversion rate. The only problem is that it relies on JavaScript to work which might be suboptimal in some cases. You could also use [Honeypot Captcha approach](https://haacked.com/archive/2007/09/11/honeypot-captcha.aspx): you can create a honeypot form field that should be left blank and then use CSS to hide it from human users, but not bots. When the form is submitted, you check to make sure the value of that form field is blank. If it isn’t, then you can safely ignore the submission because it was submitted by a spam bot.
![](https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/550ef4ab-debb-4fb4-b7ac-c9138e14145e/javascript-captcha.png)

---

- **[New Approaches To Designing Log-In Forms](https://www.smashingmagazine.com/2011/08/new-approaches-to-designing-login-forms/)** · Smashing Magazine · 2011
- **[Better Password Masking For Sign-Up Forms](https://www.smashingmagazine.com/2012/10/password-masking-hurt-signup-form/)** · Smashing Magazine · 2012
- **[UX In Contact Forms: Essentials To Turn Leads Into Conversions](https://www.smashingmagazine.com/2018/03/ux-contact-forms-essentials-conversions/)** · Smashing Magazine · 2018

---
**[Rethinking Authentication UX](https://www.smashingmagazine.com/2022/08/authentication-ux-design-guidelines/)** · Smashing Magazine · 2022
As oito rotas de recuperação de acesso, cada uma com o caso em que falha:

![A screenshot with a 'Send magic link' button](https://res.cloudinary.com/indysigner/image/fetch/f_auto,q_80/w_400/https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/bb887d40-c454-4b48-be73-44e903492deb/magic-links-authentication.jpg)

![A screenshot with a 'Send magic link' button](https://res.cloudinary.com/indysigner/image/fetch/f_auto,q_80/w_400/https://archive.smashing.media/assets/344dbf88-fdf9-42bb-adb4-46f01eedd629/d5f47188-9295-494f-bf55-f5d5a335dd9c/password-access-recovery-authentication-ux-default.jpg)
**Send a magic link for log-in via email.**
Don’t require users to retype a password, or set a new one. Users might not have access to email, or it could be hacked.

**Send a magic link for log-in to a secondary email.**
Unfortunately, the secondary email is often outdated, or the user might have no access to it.

**Send an SMS verification URL/code to a mobile phone.**
This option won’t work for users who have purchased a new phone, or don’t have access to their SIM-card (e.g. when travelling abroad).

**Send a push notification via OTP/2FA.**
This option won’t work for users who have purchased a new phone and haven’t set up OTP/2FA just yet, or don’t have access to their old phone.

**Biometric authentication via a dedicated app/Yubikey.**
This option won’t work for users who don’t have an OTP/2FA setup yet, or have purchased a new phone/Yubikey.

**Type backup recovery codes.**
Not every user will have backup recovery codes nearby, but if they do, they should always override account lock-out. Sometimes backup recovery codes are sent via a postal service, but they could be lost/stolen.

**Phone call verification.**
Users could be called on their (new) phone, and they’d need to answer a few questions to verify their identity. Ideally, it would be something that they know (e.g. latest transactions), something that they have (e.g. credit card) and something that they are (e.g. face recognition via a video call).

**Customer support inquiry.**
Ideally, users could restore access by speaking to an agent via live chat, WhatsApp/Telegram, video call or email (which is usually the slowest).

---

- **[What Is Two-Factor Authentication (2FA)?](https://www.authy.com/what-is-2fa/)** · Authy
- **[App login design: choosing the right user login option for your app](https://uxmag.com/articles/app-login-design-choosing-the-right-user-login-option-for-your-app)** · UX Magazine
- **[Passwordless Authentication Methods for SaaS Web Applications](https://www.uxmatters.com/mt/archives/2022/02/passwordless-authentication-methods-for-saas-web-applications.php)** · UXmatters · 2022

- **[Password Creation: 3 Ways To Make It Easier](https://www.nngroup.com/articles/password-creation/)** · Nielsen Norman Group
- **[HealthCare.gov's Account Setup: 10 Broken Usability Guidelines](https://www.nngroup.com/articles/affordable_care_act_usability_issues/)** · Nielsen Norman Group

---

**[Passwordless Accounts: One-Time Passwords (OTPs) and Passkeys](https://www.nngroup.com/articles/passwordless-accounts/)** · Nielsen Norman Group
**[Passwordless Accounts (vídeo)](https://www.youtube.com/watch?v=ulAbaGKqZis)** · Nielsen Norman Group

- **Offer the options of (1) creating and using a password** **and (2) biometric authentication** after users have created a passwordless account. Some users may prefer these to using an OTP or passkey, so it’s a good idea to provide the choice.
- **For OTPs, let users choose between email and text messages.** Remember that some users may have text messages delivered to their current device, while others will not.
- **For passkeys, support multiple devices by allowing users to scan a QR code.** This is especially helpful if they are using a device that doesn’t have their passkey stored on it.

![](https://media.nngroup.com/media/editor/2023/06/13/yummly-combined.png)

![](https://media.nngroup.com/media/editor/2023/06/13/waze1.PNG)


---

[Login Walls - NN Group](https://www.youtube.com/watch?v=QDHbc125x0s)
- **[A Checklist for Registration and Login Forms on Mobile](https://www.nngroup.com/articles/checklist-registration-login/)** · Nielsen Norman Group
- **[How to Achieve Painless Registration](https://www.asktog.com/columns/081Registration.html)** · Bruce Tognazzini


- **[Where to Send Users after They 'Sign In' or 'Reset Password'](https://baymard.com/premium/blog/account-sign-in-flows)** · Baymard
  34% dos sites erram esse destino. Requer assinatura.
- **[Account & Sign-In — guideline collection](https://baymard.com/premium/guideline-collections/vq05pt)** · Baymard
  Requer assinatura.
