Changelog
=========

0.6.2 (unreleased)
------------------

- Nothing changed yet.


0.6.1 (2022-09-16)
------------------

- Do not set anymore IncomingMail mail_type
  [sgeulette]

0.6.0 (2020-06-22)
------------------

- Implement basic auth for requests
  [mpeeters]


0.5.0 (2019-12-03)
------------------

- Make the dispatcher resilient to RabbitMQ restart
  [mpeeters]

- Improve logging for docker containers
  [mpeeters]


0.4.0 (2019-09-11)
------------------

- Improve request messages to handle caching
  [mpeeters]

- Implement `Email` dispatcher
  [mpeeters]


0.3.1 (2018-12-05)
------------------

- Add `error_count` attribute on `Request` object
  [mpeeters]


0.3.0 (2018-12-03)
------------------

- Add the path to the request message
  [mpeeters]


0.2.1 (2018-11-29)
------------------

- Handle missing client for publishers and add a reconnect feature
  [mpeeters]


0.2 (2016-04-22)
----------------

- Add dispatchers for deliberations and outgoing generated mails
  [mpeeters]

- Remove the invoice dispatcher since the document type no longer exist
  [mpeeters]

- Add the Response object
  [mpeeters]

- Add the Request and RequestFile objects
  [mpeeters]


0.1 (2014-10-17)
----------------

- Initial release
  [mpeeters]
