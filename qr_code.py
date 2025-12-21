{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "7b392645",
   "metadata": {},
   "outputs": [],
   "source": [
    "import qrcode\n",
    "from PIL import Image"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "cdaa38ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ QR code généré : qr_ilcli.png\n"
     ]
    }
   ],
   "source": [
    "\n",
    "# Générer le QR code\n",
    "qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)\n",
    "qr.add_data(\"ILCLI - Exemple QR Code\")\n",
    "qr.make(fit=True)\n",
    "qr_img = qr.make_image(fill_color=\"black\", back_color=\"white\").convert(\"RGBA\")\n",
    "\n",
    "# Charger un logo existant (par exemple logo.png dans ton dossier)\n",
    "logo = Image.open(\"/home/la-mus/AI/logo_ilcli.png\").convert(\"RGBA\")\n",
    "\n",
    "# Redimensionner le logo\n",
    "qr_w, qr_h = qr_img.size\n",
    "logo_size = int(qr_w * 0.25)\n",
    "logo = logo.resize((logo_size, logo_size))\n",
    "\n",
    "# Coller le logo au centre\n",
    "pos = ((qr_w - logo_size) // 2, (qr_h - logo_size) // 2)\n",
    "qr_img.alpha_composite(logo, dest=pos)\n",
    "\n",
    "# Sauvegarder l’image\n",
    "qr_img.save(\"qr_ilcli.png\")\n",
    "print(\"✅ QR code généré : qr_ilcli.png\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0bb9cf2d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "python (AI)",
   "language": "python",
   "name": "ai"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
