import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# 🚨 ЗАМЕНИ ЭТОТ ТОКЕН НА СВОЙ! 🚨
TOKEN = "7823170466:AAHFyANTJMqtfwzUW7bPXQC1edGzZqQFVXQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Команда /start
@dp.message(Command("start"))
async def start_command(message: types.Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📲 X-Poker'i indir", url="https://x-poker.net"),
         InlineKeyboardButton(text="🚀 Kulübe katıl?", url="https://i.x-mobilegame.com/AW2g")],
        [InlineKeyboardButton(text="💰 Bakiye yükle?", url="https://t.me/wallet"),
         InlineKeyboardButton(text="💵 Para çek", callback_data="payout")],
        [InlineKeyboardButton(text="📝 Kayıt yap?", callback_data="register"),
         InlineKeyboardButton(text="📞 Yardım ve iletişim", callback_data="help")]
    ])  # ✅ Закрыли список кнопок

    await message.answer("Merhaba! King34 kulübüne hoş geldiniz! Ne yapmak istersiniz?", reply_markup=keyboard)

# Команда /help
@dp.message(Command("help"))
async def help_command(message: types.Message):
    text = (
        "🔹 *King34 Kulübü Komutları* 🔹\n\n"
        "📌 *Daha fazla bilgi için aşağıdaki komutları kullanabilirsiniz:*\n\n"
        "🏆 /about \\- *King34 Kulübü Hakkında*\n"
        "📝 /register \\- *Kayıt Nasıl Olunur?*\n"
        "💰 /payin \\- *Bakiye Nasıl Yüklenir?*\n"
        "💸 /payout \\- *Para Nasıl Çekilir?*\n"
        "📜 /rules \\- *Oyun Kuralları*\n"
        "📞 /ask \\- *Destek*\n"
        "ℹ️ /help \\- *Detaylar*"
    )

    await message.answer(text, parse_mode="MarkdownV2")

# Команда /about (o клубе)
@dp.message(Command("about"))
async def about_command(message: types.Message):
    await message.answer(
        "🏆 *KingClub34 – Özel Kulüp* 🏆\n\n"
        "KingClub34, yalnızca *seçkin oyuncuların kabul edildiği özel bir poker kulübüdür*.\n"
        "Üyelik süreci *sınırlıdır* ve yalnızca *anketi başarıyla geçen* oyuncular kulübe katılabilir.\n\n"
        "📌 *Anketin amacı nedir?*\n"
        "Kulüp, *yalnızca güvenilir, saygılı ve kaliteli oyuncuların bulunduğu bir ortam yaratmayı hedefler*.\n"
        "Anket, üyelerin kulübün değerleriyle uyumlu olup olmadığını belirlemek için gereklidir.\n\n"
        "🔹 *Kimler kabul edilir?*\n"
        "✔️ Saygılı ve adil oyuncular\n"
        "✔️ Kulüp kurallarına uyan bireyler\n"
        "✔️ Pokeri sadece eğlence ve strateji olarak gören kişiler\n\n"
        "🚫 *Kimler kabul edilmez?*\n"
        "❌ Hile yapmaya meyilli oyuncular\n"
        "❌ Kulüp kurallarına ve topluluk değerlerine saygı göstermeyenler\n"
        "❌ Sorumluluk bilinci olmayan kişiler\n\n"
        "Kulüp üyeleri için *en iyi poker deneyimini sağlamak amacıyla güvenli, adil ve kaliteli bir oyun ortamı oluşturulmuştur*.\n"
        "Eğer siz de bu özel topluluğun bir parçası olmak istiyorsanız, *ön eleme sürecini tamamlamanız gerekmektedir*.\n\n"
        "📩 Daha fazla bilgi ve başvuru için yöneticimizle iletişime geçin.🚀 https://t.me/no_mad_games"
    )

# Команда /payin (пополнить баланс)
@dp.message(Command("payin"))
async def payin_command(message: types.Message):
    await message.answer(
    "Standart yükleme yöntemlerimiz: USDT TRC20 veya Papara.\n"
    "💰@Wallet üzerinden ödeme yapmak için, ödemeyi şu adrese gönderin: @Bombay_temsilcisi.\n"
    "Ödeme yapıldıktan sonra ID numaranızı aynı adrese yollayın.\n"
    "Fişler birkaç dakika içinde hesabınıza yüklenecektir.\n"
    "💬 Papara ile ödeme yapmak için yöneticimizle iletişime geçin: https://t.me/no_mad_games\n"
    "          1 çip = 10 TL      "
) 

# Команда /payout (вывод средств)
@dp.message(Command("payout"))
async def payout_command(message: types.Message):
    await message.answer(
        "💸 Para Çekme İşlemi – Sadece Salı Günleri 💸\n\n"
        "📌 Kulübümüz özel bir sistemle çalışmaktadır.\n"
        "🚫 Salı günü kulüp kapalıdır, oyunlar açılmaz.\n\n"
        "🔹 Para çekmek için yöneticimize şu bilgileri gönderin:\n"
        "✅ ID Numarası\n"
        "✅ Wallet adresi veya Papara numarası\n"
        "✅ Çekmek istediğiniz tutar\n\n"
        "📩 Bilgileri buraya gönderin: @no_mad_games\n\n"
        "💰 İşlem Süreci:\n"
        "1️⃣ Salı günü kulüp kapatılır, oyunlar durdurulur.\n"
        "2️⃣ Hesabınızdaki fişler çekilir.\n"
        "3️⃣ Belirtilen tutar tarafınıza ödenir.\n\n"
        "🚀 Ödeme günü: Sadece Salı!"
    )

# Команда /rules (правила)
@dp.message(Command("rules"))
async def rules_command(message: types.Message):
    await message.answer(
        "📜 *King34 Oyun Kuralları* 📜\n\n"
        "King34 kulübünde *adil ve kaliteli bir oyun ortamı* sağlamak için belirli kurallar uygulanmaktadır.\n"
        "Aşağıda oyun süreci ve kurallar hakkında detaylı bilgi bulabilirsiniz.\n\n"
        "📌 *Call Time (Minimum 1 Saat) Nedir?*\n"
        "✔️ *Call Time*, oyuncuların masada kalmasını ve oyun sürekliliğini sağlamak için kullanılan bir sistemdir.\n"
        "✔️ Minimum *1 saat* Call Time zorunludur.\n"
        "✔️ Oyuncular *1 saatten önce masadan çıkamaz*.\n"
        "✔️ Eğer bir oyuncu *erken ayrılmak zorunda kalırsa*, masadan çıkabilir ancak *Call Time bitene kadar veya kazanç miktarı sıfırlanana kadar kör bahisler düşmeye devam eder*.\n\n"
        "📌 *Kazançlı duruma geçtiğinizde, Call Time'ı başlatmayı unutmayın!*\n"
        "*Sol üst köşedeki menüden 'Call Time' seçeneğini kullanarak aktif hale getirin.*\n\n"
        "📌 *Oyun Günleri ve Ödeme Sistemi*\n"
        "✔️ *Oyunlar her Çarşamba başlar ve Pazartesi sona erer.*\n"
        "✔️ *Salı günü oyunlar kapalıdır ve ödeme günü olarak belirlenmiştir.*\n"
        "✔️ *Ödemeler yalnızca Salı günü yapılır.*\n\n"
        "📌 *Çip Değeri*\n"
        "💰 1 çip = *10 TL*\n\n"
        "📌 *Kör Bahisler ve Minimum Buy-in*\n"
        "🃏 *Texas Hold'em:*\n"
        "🔹 Kör Bahisler: *50/100 TL*\n"
        "🔹 Minimum Buy-in: *3000 TL*\n\n"
        "🎲 *Pot Limit Omaha:*\n"
        "🔹 Kör Bahisler: *30/60 TL*\n"
        "🔹 Minimum Buy-in: *1800 TL*\n\n"
        "📩 *Daha fazla bilgi için yöneticimizle iletişime geçin:* https://t.me/no_mad_games\n\n"
        "🚀 *Adil ve kaliteli oyun için King34 kurallarına uyunuz!*"
    )

# Команда /ask (связь с кассой)
@dp.message(Command("ask"))
async def ask_command(message: types.Message):
    await message.answer("Kasayla iletişime geçmek için destek ekibimize yazabilirsiniz: https://t.me/no_mad_games")

# Команда /register (регистрация)
@dp.message(Command("register"))
async def play_command(message: types.Message):
    await message.answer(
        "🏆 *King34 Kulübüne Nasıl Kayıt Olurum?* 🏆\n\n"
        "King34, yalnızca *seçkin oyuncuların kabul edildiği özel bir poker kulübüdür*.\n"
        "Kulübe katılmak için aşağıdaki bilgileri sağlamanız ve ön eleme sürecini tamamlamanız gerekmektedir.\n\n"
        "📌 *Başvuru İçin Gerekli Bilgiler:*\n"
        "✔️ *Adınız ve Soyadınız*\n"
        "✔️ *Doğum Tarihiniz* (18 yaş ve üzeri zorunludur)\n"
        "✔️ *E-posta Adresiniz*\n"
        "✔️ *WhatsApp Numaranız*\n"
        "✔️ *Poker Deneyiminiz* (kaç yıldır oynuyorsunuz?)\n"
        "✔️ *Oynamak İstediğiniz Limitler*\n\n"
        "📸 Kullanıcı adınızın ve ID’nizin ekran görüntüsünü alarak @no_mad_games adresine gönderin.\n\n"
        "📌 *Başvurunuzu yöneticimize ilettiğinizde, kulüp kurallarını kabul ettiğinizi onaylamış olursunuz.*\n\n"
        "🚀 *King34 yalnızca seçkin oyunculara açıktır!*"
    )

# Обработчик нажатий на Inline-кнопки
@dp.callback_query()
async def handle_buttons(callback: types.CallbackQuery):
    if callback.data == "payin":
        await callback.message.answer("Bakiye yüklemek için yöneticimizle iletişime geçin.https://t.me/no_mad_games")
    elif callback.data == "payout":
        await callback.message.answer("💵 Para çekme işlemi için lütfen destek ekibiyle iletişime geçin: https://t.me/no_mad_games")
    elif callback.data == "register":
        await callback.message.answer(
            "🏆 *King34 Kulübüne Nasıl Kayıt Olurum?* 🏆\n\n"
            "King34, yalnızca *seçkin oyuncuların kabul edildiği özel bir poker kulübüdür*.\n"
            "Kulübe katılmak için aşağıdaki bilgileri sağlamanız ve ön eleme sürecini tamamlamanız gerekmektedir.\n\n"
            "📌 *Başvuru İçin Gerekli Bilgiler:*\n"
            "✔️ *Adınız ve Soyadınız*\n"
            "✔️ *Doğum Tarihiniz* (18 yaş ve üzeri zorunludur)\n"
            "✔️ *E-posta Adresiniz*\n"
            "✔️ *WhatsApp Numaranız*\n"
            "✔️ *Poker Deneyiminiz* (kaç yıldır oynuyorsunuz?)\n"
            "✔️ *Oynamak İstediğiniz Limitler*\n\n"
            "📸 Kullanıcı adınızın ve ID’nizin ekran görüntüsünü alarak @no_mad_games adresine gönderin.\n\n"
            "📌 *Başvurunuzu yöneticimize ilettiğinizde, kulüp kurallarını kabul ettiğinizi onaylamış olursunuz.*\n\n"
            "📩 *Başvuru için yöneticimizle iletişime geçin:* https://t.me/no_mad_games\n\n"
            "🚀 *King34 yalnızca seçkin oyunculara açıktır!*"
        )
    elif callback.data == "help":
        await callback.message.answer("Herhangi bir sorunuz varsa destek ekibimizle iletişime geçebilirsiniz.https://t.me/no_mad_games")

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
