import pyChatGPT

session_token = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..mx5e65E_q35YMhNy.F4eeZmAdMHfF0N7_RROmabs5ArJeo_WezYOAgFTQhUL6F" \
                "mJyWgOrxmotXGVp8cbCn4-Fw5LyZgJWsO7XqReBjuPpwmufYDGEpV5gdf9D-6Bmdsb0lHQA8kiTs0UIMBlRJyFj25u5tR9_d30wcaZm3" \
                "BoH_L7AdZInN5tYk8_goChHUdkRkdfv9Aows6_ubufqz8hNleh50M2OcCQFMcKgy07Xj0CAZULa8SXaT0onAekIbX5vtxwcyI6xODg6V" \
                "wtXwNQ2GV68djexCh43cskkW19vvvpeYDk38d_9z2StvtV0pZx2uxsuiuC7SpuyAln44Nx9H1TdUJf50af2c-tof6EnZRnR2gWMS8-XQ" \
                "ElcfB76m_GkIRj2B4E7dV6Nw0q7kB8VZsYiwvD7d9o3OEOrXMmcfVCyx_lWAnDRL6SAjVA05yXsuIvY5HLYV4yz8be1CIfoluS1lqE6u" \
                "Uk_gMVDCHOcI-dEba4PovFB3BvnDA5t3ISqOSiS7XqIjBLmNyuo6mOT2o5M-XovLWO1srETbeW1LuYn3OfWyw5bljvxRaoBpqrYqy9GJ" \
                "590QL2lNFhZ-RWwJUUc9JxKvjeNBeps51W3b0dNozvLJPqg1F5Ka2rrpwANXWJ4dysGL9OK2GvBhTWk5e4OUqQ8wYLWIED8oyWyShCBG" \
                "Ajwoo-AXEuf3AcMZ3u-pBXlfnJtb4IDN5SYDbq7ehj96aDKIGWvzGYFjqGct4jUAjTjcjy0fiz806b_gSev08hDfA4QpHdIkQVyEBEKV" \
                "lDj5xm5AwlImJDCnItmqmN5Yf5EW5ck8CMa6aRafilNnK6OeuhwkmJis7UueBXLf4_u210QaOxII5pTI_LtmEuy9Uu_CWGwd_AeoDU7l" \
                "Uc3QWL1_PpHNvvv4zw6mlM0bv1NgtmR5gzBpd0KIKpTsKNLZX5YhmMdumlD61JIkw6n5r38wL1dy7u98KJ6WaWqoyCbODu-qv6TmXUWd" \
                "56U7rNcfgjMBRpXEh41gpDoDtkESZZiZSvFI2Z6enWmBcEhUkhxTE2x2AVLhL7naC5Xvu7yXmdNuBGnWqWnm1hL8AMHqke5XE_Vw5XG8" \
                "9-Rv5FGQnMBMxCFd7gfZzVrK8JUhk-US_EHQ-rutnExiLfw7FIhvysjvn20m-xeXvnaZ1QIGS-bEbxz1z8HkJRkc0cTHitQ4oOvdoDYj" \
                "4uFnbaGN956E_dEZ8ASfOq97WLe1bNb-R7mOYpwxHf9RK2Wlh-dR4gJp39kYdFLShtHyh850pIQmfrB85nAeipVw0egfb9_wF2G22ptW" \
                "4E38poNy1-VVowaFkrOTZYVXvXyT05QZ0I41_syEWoc2ceo753u4yZQrmGPAgXsyuw_sWlafa5mQfRqoaGh1pi9epzZZ_AE7O5UIFC13" \
                "DY-1g9NGSMPtnZBiRGLyLeiiXwsti76wRUc2b5ZKA5k4A1G_4N7-Ugo3nycXLlhO0maovx-UH_NafAHnsTWqMepE_csnXyJoYXWn9Roc" \
                "x5qmWuBoEGn2BjyzI7Wk70fuXpKU6vPDtqbQSuA_uHadbSgntsWneuWHhjcliLLljA1JDaEDXwudWsAjCW2Kk6QmzvnwVduk8WCjlG4Y" \
                "5yupTMcpmFTaDIrthw1bzdkqI1X-cSs6P_nCb_LreZ-IH_Gf5MIgHuqqde2JH7M044jKteoVuDuP8ylNzI11Zjx0ADdniVBYuew9cpWW" \
                "sYcB-y57H3MNsfrMoSOmKYlOCBHZB1AhI8k3NDrGpX_e3T6r7hGocYD0V7L6mKQ1XENJ6c-hHJpl3IYnkvSaBHYWP8-JQsjYhBS6eoN" \
                "pVYv95PtIE4szPZyGbZIGddEYMXNxYyGaqha7jK7Z3wli41U0HWF0g5SPhu8JwpmNUfm74h-XyLyv0hweDF-840ASmy5DYGeHgV_Qux" \
                "zvoECs0ddlTTAA2CKcxMIaDaBlCAmeB7NlTOzXE7Kb3auDU-dNmrMVouuO61vuvXP4GrSxU9ZNMNRDLryhRLakrU_eRvZS1gJEX-5j8" \
                "-JiZFuiWKPMqYZ-Hf0imkb_G4IQ0PvHj0wiCRy0AZ2oO0_HreUqnXDeQJOGZiz4UjojN4oM0OqNBY4ttgSR77fawtREZABeABrlLWgu" \
                "GVE2NN0CDX_JbOXiPorlaWO6n7unBCFcC33ZdgQXnvI5iTiQg5x6ka-IokMEIaUIgskEraRWSWwJNn7MuhJG0kJ1O1sFlfMbzLLMQYe" \
                "n-U-j7SlFyzS1EHxKYlaNLlFAdwhjtU9M6Q28HeV-p2JfQ.8MpB830EqcKdadUatHWBsw"
session_api = pyChatGPT.ChatGPT(session_token=session_token)

run = True
while run:
    request = input("Type your query: ")
    response = session_api.send_message(request)

    response = "".join(response.get('message'))
    print()
    print(response)
    print()

    run = bool(input('Do you want to continue?'))
    print()
print('Thank you')

# # getting the message from user
# request = input("Type your query: ")
#
# # requesting to the ChatGPT
# response = session_api.send_message(request)
#
# # printing the response
# print(response)
