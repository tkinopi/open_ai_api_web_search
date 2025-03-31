import json
import openai

# OpenAIのクライアント設定（APIキーをセット）
client = openai.OpenAI(
    api_key=""
)


def search_web(query):
    """Web検索を使って最新情報を取得する関数"""
    response = client.chat.completions.create(
        model="gpt-4o-search-preview",
        web_search_options={
            "search_context_size": "medium",  # 検索深度
            "user_location": {
                "type": "approximate",
                "approximate": {
                    "country": "JP",  # 地域
                },
            },
        },
        messages=[ {"role": "system","content": "以下に示す各企業の職種についてWeb検索を行い、その内容を簡潔にまとめてください。番号ごとにまとめ、各企業ごとに2～3行程度で要点を記述してください。"},{"role": "user", "content": query}],
    )

    return response.choices[0].message.content


def lambda_handler(event, context):
    result = search_web("#2\n会社名: opsol株式会社　パリアティブケアホーム　ほしの岸和田職種: 常勤（夜勤あり）の施設内訪問看護\n\n #3\n会社名: opsol株式会社　パリアティブケアホームゆきの彩都 職種: 常勤（夜勤あり）の施設内訪問看護 #4\n会社名: あい・さくらホーム大阪株式会社　あい・さくらホーム東住吉 職種: 日勤常勤の施設内訪問看護")
    # TODO implement
    print(result)
    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }
