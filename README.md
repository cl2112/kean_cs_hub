# Secure_OCIS_Online
Project for CPS 4301-01: Software Engineering at Kean University.

## Goal
The goal of this project is to convert any pages served as HTTP to HTTPS for the Kean OCIS online services, starting with the Eve server account page because it is a single page that would offer the most benefit from upgrading.

## Plan
(Tentative)
- Copy the Eve account web page and map to a different URL for testing.
- Upgrade the page and all linked pages to HTTPS.
- Test that the page is working correctly.
- Have the original, HTTP version URL redirect to the new HTTPS version, doing a gradual rollout if possible.
- Then, after more testing and confirmation of the Eve account page, do a crawl of the rest of the OCIS service pages to find additional HTTP pages.

## Some Resources
[The Complete Guide To Switching From HTTP To HTTPS - Smashing Magazine](https://www.smashingmagazine.com/2017/06/guide-switching-http-https/)
[How do I convert my site to SSL and HTTPS? Internet security: secure websites with SSL and HTTPS - Ionos](https://www.ionos.com/digitalguide/websites/website-creation/how-do-i-convert-my-site-to-ssl-and-https/)
[Guide: Converting Your Site From HTTP to HTTPS - Elevated](https://www.elevated.com/guide-converting-site-http-https/)
[How to Convert HTTP to HTTPS: A Quick Guide - Brafton](https://www.brafton.com/blog/distribution/how-to-convert-http-to-https-a-quick-guide/)

