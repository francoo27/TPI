import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


gmail_user = 'cinearventassistema@gmail.com'
gmail_password = 'cinear123'

def sendmail(data):
    tipoPrecios =[]
    print(len(data.tickets))
    for t in data.tickets:
        if len(tipoPrecios) < 1:
          tipoPrecios.append({"id":t.precio.id_tipoPrecio,"nombre":t.precio.tipoPrecio.nombre,"valor":t.precio.valor,"cantidad":1})
          continue
        for tp in tipoPrecios:
            item = list(filter(lambda tp: tp['id'] == t.precio.id_tipoPrecio, tipoPrecios))
            if len(item) < 1:
                tipoPrecios.append({"id":t.precio.id_tipoPrecio,"nombre":t.precio.tipoPrecio.nombre,"valor":t.precio.valor,"cantidad":1})
                break
            else:
                tp.update({"cantidad":tp["cantidad"]+1})
                break

            
    print(tipoPrecios)
    middleTemplate =""
    total = 0
    emailTemplate = mailTopTemplate
    for tp in tipoPrecios:
      middleTemplate+= getTicketRowTemplate(tp["nombre"],tp["cantidad"],tp["cantidad"]*tp["valor"])
      total +=tp["cantidad"]*tp["valor"]
    
    emailTemplate+= middleTemplate 
    emailTemplate+= getTicketTotalTemplate(total)
    emailTemplate+= bottonTemplate
    sent_from = gmail_user
    to = ['cinearventassistema@gmail.com']
    subject = 'OMG Super Important Message'
    body = "'Hey, what's up?\n\n- You'"

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(data.email), subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, data.email, MIMEText(emailTemplate, 'html').as_string())
        server.close()

        print('Email sent!')
    except:
        print('Something went wrong...')



def getTicketRowTemplate(tipo,cantidad,subtotal):
  return f"""<div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;">
              <div class="u-row">

                <div class="u-col u-col-33p33">
                  <div style="padding: 0px;border-top: 2px solid #CCC;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 2px solid #CCC;border-radius: 0px;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%;">{tipo}</p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

                <div class="u-col u-col-33p33">
                  <div style="padding: 0px;border-top: 2px solid #CCC;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 2px solid #CCC;border-radius: 0px;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%;">{cantidad}</p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

                <div class="u-col u-col-33p33">
                  <div style="padding: 0px;border-top: 2px solid #CCC;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 2px solid #CCC;border-radius: 0px;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%;">{subtotal}</p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>"""

def getTicketTotalTemplate(total):
  return f"""          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 2px solid #000000;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 2px solid #000000;border-radius: 0px;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%; text-align: right;"><b>TOTAL   ${total}</b></p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>"""



mailTopTemplate = """
<!doctype html>
<html ⚡4email data-css-strict>

<head>
  <meta charset="utf-8">
  <meta name="x-apple-disable-message-reformatting">
  <style amp4email-boilerplate>
    body {
      visibility: hidden
    }
  </style>

  <script async src="https://cdn.ampproject.org/v0.js"></script>


  <style amp-custom>
    table,
    td {
      color: #000000;
    }
    
    a {
      color: #0000ee;
      text-decoration: underline;
    }
    
    .u-row {
      display: flex;
      flex-wrap: nowrap;
      margin-left: 0;
      margin-right: 0;
    }
    
    .u-row .u-col {
      position: relative;
      width: 100%;
      padding-right: 0;
      padding-left: 0;
    }
    
    .u-row .u-col.u-col-33p33 {
      flex: 0 0 33.33%;
      max-width: 33.33%;
    }
    
    .u-row .u-col.u-col-100 {
      flex: 0 0 100%;
      max-width: 100%;
    }
    
    @media (max-width: 767px) {
      .u-row:not(.no-stack) {
        flex-wrap: wrap;
      }
      .u-row:not(.no-stack) .u-col {
        flex: 0 0 100%;
        max-width: 100%;
      }
    }
    
    body {
      margin: 0;
      padding: 0;
    }
    
    table,
    tr,
    td {
      vertical-align: top;
      border-collapse: collapse;
    }
    
    p {
      margin: 0;
    }
    
    .ie-container table,
    .mso-container table {
      table-layout: fixed;
    }
    
    * {
      line-height: inherit;
    }
  </style>


</head>

<body class="clean-body u_body" style="margin: 0;padding: 0;background-color: #f9f9f9;color: #000000">
  <!--[if IE]><div class="ie-container"><![endif]-->
  <!--[if mso]><div class="mso-container"><![endif]-->
  <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f9f9f9;width:100%" cellpadding="0" cellspacing="0">
    <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse;vertical-align: top">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f9f9f9;"><![endif]-->

          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="color: #afb0c7; line-height: 170%; text-align: center; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 170%;"><span style="font-size: 14px; line-height: 23.8px;">View Email in Browser</span></p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>

          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;background-color: #ffffff;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;background-color:#ffffff;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%; text-align: center;"><span style="font-size: 28px; line-height: 39.2px; font-family: Lato, sans-serif;"><span style="color: #236fa1; line-height: 39.2px; font-size: 28px;">CINE</span> <span style="color: #f1c40f; line-height: 39.2px; font-size: 28px;">AR</span></span>
                              </p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>

          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;background-color: #003399;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:40px 10px 10px;font-family:'Cabin',sans-serif;" align="left">

                            <table width="100%" cellpadding="0" cellspacing="0" border="0">
                              <tr>
                                <td style="padding-right: 0px;padding-left: 0px;" align="center">

                                  <amp-img alt="Image" src="https://cdn.templates.unlayer.com/assets/1597218650916-xxxxc.png" width="335" height="93" layout="intrinsic" style="width: 26%;max-width: 26%;">

                                  </amp-img>
                                </td>
                              </tr>
                            </table>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="color: #e5eaf5; line-height: 140%; text-align: center; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%;"><strong>Gracias por tu compra !</strong></p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:0px 10px 31px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="color: #e5eaf5; line-height: 140%; text-align: center; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 28px; line-height: 39.2px;"><strong><span style="line-height: 39.2px; font-size: 28px;">COMPRA EXITOSA</span></strong>
                                </span>
                              </p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>

          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 2px solid #000000;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 2px solid #000000;border-radius: 0px;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <h1 style="margin: 0px; line-height: 140%; text-align: left; word-wrap: break-word; font-weight: normal; font-family: arial,helvetica,sans-serif; font-size: 22px;">
                              Ticket
                            </h1>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>"""



bottonTemplate ="""
          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;background-color: #ffffff;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:33px 55px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 160%; text-align: center; word-wrap: break-word;">
                              <p style="line-height: 160%; font-size: 14px;"><span style="font-size: 22px; line-height: 35.2px;">Te adjuntamos abajo los tickets de tu compra</span></p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:33px 55px 60px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="line-height: 160%; text-align: center; word-wrap: break-word;">

                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>

          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;background-color: #e5eaf5;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:41px 55px 18px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="color: #003399; line-height: 160%; text-align: center; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 20px; line-height: 32px;"><strong>Get in touch</strong></span></p>
                              <p style="font-size: 14px; line-height: 160%;"><span style="font-size: 16px; line-height: 25.6px; color: #000000;">+11 111 333 4444</span></p>
                              <p style="font-size: 14px; line-height: 160%;">cinearventassistema@gmail.com</p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px 10px 33px;font-family:'Cabin',sans-serif;" align="left">
                            <div style="text-align:center;line-height:0px">
                              <a href="https://facebook.com/" target="_blank" style="display:inline-block;width:32px;height:32px;margin-right:17px">
                                <amp-img src="https://cdn.tools.unlayer.com/social/icons/circle-black/facebook.png" width="32" height="32" />
                              </a>
                              <a href="https://linkedin.com/" target="_blank" style="display:inline-block;width:32px;height:32px;margin-right:17px">
                                <amp-img src="https://cdn.tools.unlayer.com/social/icons/circle-black/linkedin.png" width="32" height="32" />
                              </a>
                              <a href="https://instagram.com/" target="_blank" style="display:inline-block;width:32px;height:32px;margin-right:17px">
                                <amp-img src="https://cdn.tools.unlayer.com/social/icons/circle-black/instagram.png" width="32" height="32" />
                              </a>
                              <a href="https://youtube.com/" target="_blank" style="display:inline-block;width:32px;height:32px;margin-right:17px">
                                <amp-img src="https://cdn.tools.unlayer.com/social/icons/circle-black/youtube.png" width="32" height="32" />
                              </a>
                              <a href="https://email.com/" target="_blank" style="display:inline-block;width:32px;height:32px;margin-right:0px">
                                <amp-img src="https://cdn.tools.unlayer.com/social/icons/circle-black/email.png" width="32" height="32" />
                              </a>
                            </div>
                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>

          <div style="padding: 0px;">
            <div style="max-width: 600px;margin: 0 auto;background-color: #003399;">
              <div class="u-row">

                <div class="u-col u-col-100">
                  <div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;">

                    <table style="font-family:'Cabin',sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                      <tbody>
                        <tr>
                          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:'Cabin',sans-serif;" align="left">

                            <div style="color: #fafafa; line-height: 180%; text-align: center; word-wrap: break-word;">
                              <p style="font-size: 14px; line-height: 180%;"><span style="font-size: 16px; line-height: 28.8px;">Copyrights &copy; Todos los derechos reservados</span></p>
                            </div>

                          </td>
                        </tr>
                      </tbody>
                    </table>

                  </div>
                </div>

              </div>
            </div>
          </div>

          <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
      </tr>
    </tbody>
  </table>
  <!--[if mso]></div><![endif]-->
  <!--[if IE]></div><![endif]-->
</body>

</html>
"""