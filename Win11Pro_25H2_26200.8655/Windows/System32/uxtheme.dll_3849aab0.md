# Binary Specification: uxtheme.dll

## Binary Metadata
* **Original Path:** `C:\Windows\System32\uxtheme.dll`
* **Architecture:** x64
* **SHA256 Fingerprint:** `3849aab05f6f36cd607579b70889fe727b5c8c489080a3bbd84865abffed4c87`
* **Total Exported Functions:** 199

## Exported Interface Map
| Ordinal | Export Name | Relative Virtual Address (RVA) | Function Size (Bytes) | Size Calculation Method | Notes / Forward Target |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 2 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#440` |
| 3 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#441` |
| 4 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#445` |
| 11 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#190` |
| 13 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#444` |
| 18 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#189` |
| 19 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#188` |
| 20 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#395` |
| 21 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#396` |
| 22 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#397` |
| 23 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#398` |
| 24 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#399` |
| 25 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#400` |
| 26 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#215` |
| 27 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#401` |
| 28 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#402` |
| 29 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#213` |
| 30 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#403` |
| 31 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#431` |
| 32 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#406` |
| 34 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#407` |
| 35 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#408` |
| 62 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#409` |
| 63 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#404` |
| 66 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#405` |
| 77 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#432` |
| 78 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#433` |
| 79 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#434` |
| 80 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#435` |
| 81 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#430` |
| 82 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#436` |
| 83 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#437` |
| 87 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#438` |
| 88 | *Ordinal Only* | `0x0` | - | Forwarded | Forwarded to: `SHUNIMPL.#439` |
| 128 | *Ordinal Only* | `0x2010` | 17 | UnwindData |  |
| 153 | `GetThemeAppProperties` | `0x4BB0` | 91 | UnwindData |  |
| 198 | `ThemeInitApiHook` | `0x55C0` | 894 | UnwindData |  |
| 104 | *Ordinal Only* | `0x6340` | 340 | UnwindData |  |
| 121 | `GetColorFromPreference` | `0x6690` | 445 | UnwindData |  |
| 106 | *Ordinal Only* | `0x6860` | 105 | UnwindData |  |
| 95 | `GetImmersiveColorFromColorSetEx` | `0x6D90` | 969 | UnwindData |  |
| 120 | `GetUserColorPreference` | `0x71C0` | 20 | UnwindData |  |
| 98 | `GetImmersiveUserColorSetPreference` | `0x71E0` | 40 | UnwindData |  |
| 51 | `CloseThemeData` | `0xB320` | 6,096 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 150 | `GetCurrentThemeName` | `0xCAF0` | 391 | UnwindData |  |
| 89 | `EnableThemeDialogTexture` | `0xCC80` | 200 | UnwindData |  |
| 49 | *Ordinal Only* | `0xCD50` | 61 | UnwindData |  |
| 194 | `OpenThemeDataForDpi` | `0xCE30` | 108 | UnwindData |  |
| 188 | `IsCompositionActive` | `0xCEB0` | 39 | UnwindData |  |
| 193 | `OpenThemeData` | `0xCF40` | 119 | UnwindData |  |
| 93 | *Ordinal Only* | `0xFDA0` | 15 | UnwindData |  |
| 92 | *Ordinal Only* | `0x112A0` | 321 | UnwindData |  |
| 43 | *Ordinal Only* | `0x14D80` | 73 | UnwindData |  |
| 44 | *Ordinal Only* | `0x15C00` | 118 | UnwindData |  |
| 59 | `DrawThemeParentBackgroundEx` | `0x17B60` | 102 | UnwindData |  |
| 37 | `BufferedPaintClear` | `0x1A340` | 180 | UnwindData |  |
| 158 | `GetThemeBool` | `0x1A480` | 465 | UnwindData |  |
| 155 | `GetThemeBackgroundExtent` | `0x1A660` | 456 | UnwindData |  |
| 166 | `GetThemeMargins` | `0x1A830` | 1,374 | UnwindData |  |
| 164 | `GetThemeInt` | `0x1ADA0` | 464 | UnwindData |  |
| 187 | `IsAppThemed` | `0x1AF80` | 40 | UnwindData |  |
| 71 | `DrawThemeTextEx` | `0x1AFB0` | 789 | UnwindData |  |
| 47 | `DrawThemeBackgroundEx` | `0x1B340` | 961 | UnwindData |  |
| 159 | `GetThemeColor` | `0x1B710` | 56 | UnwindData |  |
| 192 | `IsThemePartDefined` | `0x1B920` | 662 | UnwindData |  |
| 154 | `GetThemeBackgroundContentRect` | `0x1BBC0` | 1,563 | UnwindData |  |
| 189 | `IsThemeActive` | `0x1C1F0` | 172 | UnwindData |  |
| 146 | `GetBufferedPaintBits` | `0x1C2B0` | 220 | UnwindData |  |
| 168 | `GetThemePartSize` | `0x1C470` | 261 | UnwindData |  |
| 190 | `IsThemeBackgroundPartiallyTransparent` | `0x1D650` | 611 | UnwindData |  |
| 55 | `DrawThemeBackground` | `0x1DC90` | 2,048 | UnwindData |  |
| 156 | `GetThemeBackgroundRegion` | `0x20140` | 298 | UnwindData |  |
| 85 | *Ordinal Only* | `0x20A40` | 953 | UnwindData |  |
| 42 | `BufferedPaintUnInit` | `0x22100` | 49 | UnwindData |  |
| 41 | `BufferedPaintStopAllAnimations` | `0x22680` | 82 | UnwindData |  |
| 38 | `BufferedPaintInit` | `0x226E0` | 49 | UnwindData |  |
| 114 | `EndBufferedAnimation` | `0x22950` | 114 | UnwindData |  |
| 5 | `BeginBufferedAnimation` | `0x22A90` | 282 | UnwindData |  |
| 148 | `GetBufferedPaintTargetDC` | `0x22BB0` | 136 | UnwindData |  |
| 39 | `BufferedPaintRenderAnimation` | `0x22C40` | 147 | UnwindData |  |
| 147 | `GetBufferedPaintDC` | `0x22D20` | 137 | UnwindData |  |
| 126 | *Ordinal Only* | `0x22DB0` | 2,317 | UnwindData |  |
| 129 | `EndBufferedPaint` | `0x23700` | 903 | UnwindData |  |
| 6 | `BeginBufferedPaint` | `0x24430` | 304 | UnwindData |  |
| 163 | `GetThemeFont` | `0x26D60` | 802 | UnwindData |  |
| 182 | `GetThemeTextMetrics` | `0x2BF70` | 199 | UnwindData |  |
| 167 | `GetThemeMetric` | `0x2C450` | 180 | UnwindData |  |
| 186 | `HitTestThemeBackground` | `0x2C510` | 282 | UnwindData |  |
| 161 | `GetThemeEnumValue` | `0x2C630` | 160 | UnwindData |  |
| 70 | `DrawThemeText` | `0x2C6E0` | 318 | UnwindData |  |
| 151 | `GetThemeAnimationProperty` | `0x2C830` | 655 | UnwindData |  |
| 181 | `GetThemeTextExtent` | `0x2CAD0` | 620 | UnwindData |  |
| 56 | `DrawThemeEdge` | `0x2EFB0` | 281 | UnwindData |  |
| 45 | *Ordinal Only* | `0x30A00` | 197 | UnwindData |  |
| 119 | *Ordinal Only* | `0x32920` | 42 | UnwindData |  |
| 131 | *Ordinal Only* | `0x344E0` | 258 | UnwindData |  |
| 170 | `GetThemePropertyOrigin` | `0x345F0` | 160 | UnwindData |  |
| 152 | `GetThemeAnimationTransform` | `0x348E0` | 774 | UnwindData |  |
| 157 | `GetThemeBitmap` | `0x34C30` | 223 | UnwindData |  |
| 40 | `BufferedPaintSetAlpha` | `0x35D90` | 133 | UnwindData |  |
| 132 | *Ordinal Only* | `0x35EC0` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 137 | *Ordinal Only* | `0x35EF0` | 88 | UnwindData |  |
| 196 | `SetWindowTheme` | `0x36310` | 182 | UnwindData |  |
| 183 | `GetThemeTimingFunction` | `0x36DA0` | 535 | UnwindData |  |
| 75 | *Ordinal Only* | `0x3A920` | 87 | UnwindData |  |
| 171 | `GetThemeRect` | `0x3B2C0` | 507 | UnwindData |  |
| 74 | *Ordinal Only* | `0x3B910` | 375 | UnwindData |  |
| 10 | *Ordinal Only* | `0x3BA90` | 228 | UnwindData |  |
| 69 | *Ordinal Only* | `0x3BB80` | 189 | UnwindData |  |
| 9 | *Ordinal Only* | `0x3C030` | 302 | UnwindData |  |
| 58 | `DrawThemeParentBackground` | `0x41CF0` | 2,608 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 184 | `GetThemeTransitionDuration` | `0x42720` | 149 | UnwindData |  |
| 139 | *Ordinal Only* | `0x42F90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 138 | *Ordinal Only* | `0x42FB0` | 314 | UnwindData |  |
| 96 | *Ordinal Only* | `0x43AA0` | 103 | UnwindData |  |
| 169 | `GetThemePosition` | `0x453A0` | 160 | UnwindData |  |
| 172 | `GetThemeStream` | `0x45C40` | 194 | UnwindData |  |
| 177 | `GetThemeSysFont` | `0x46AD0` | 755 | UnwindData |  |
| 197 | `SetWindowThemeAttribute` | `0x46F80` | 234 | UnwindData |  |
| 175 | `GetThemeSysColor` | `0x47640` | 215 | UnwindData |  |
| 16 | *Ordinal Only* | `0x47860` | 230 | UnwindData |  |
| 57 | `DrawThemeIcon` | `0x48630` | 235 | UnwindData |  |
| 72 | *Ordinal Only* | `0x48730` | 644 | UnwindData |  |
| 179 | `GetThemeSysSize` | `0x48E60` | 198 | UnwindData |  |
| 135 | *Ordinal Only* | `0x48FF0` | 1,424 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 76 | *Ordinal Only* | `0x49580` | 34 | UnwindData |  |
| 133 | *Ordinal Only* | `0x49DE0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 185 | `GetWindowTheme` | `0x49DF0` | 148 | UnwindData |  |
| 123 | *Ordinal Only* | `0x49F10` | 97 | UnwindData |  |
| 84 | *Ordinal Only* | `0x49FF0` | 90 | UnwindData |  |
| 99 | *Ordinal Only* | `0x4A050` | 54 | UnwindData |  |
| 61 | `OpenThemeDataEx` | `0x4B080` | 82 | UnwindData |  |
| 125 | *Ordinal Only* | `0x4B1F0` | 496 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 91 | *Ordinal Only* | `0x4B3E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 101 | *Ordinal Only* | `0x4B3F0` | 896 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 136 | *Ordinal Only* | `0x4B770` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 195 | `SetThemeAppProperties` | `0x4B780` | 136 | UnwindData |  |
| 122 | *Ordinal Only* | `0x4B840` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 174 | `GetThemeSysBool` | `0x4B850` | 183 | UnwindData |  |
| 140 | *Ordinal Only* | `0x4C0B0` | 93 | UnwindData |  |
| 33 | *Ordinal Only* | `0x4EE70` | 1,520 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 199 | `UpdatePanningFeedback` | `0x4F460` | 672 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 94 | *Ordinal Only* | `0x4F700` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 117 | *Ordinal Only* | `0x4F700` | 80 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 134 | `EndPanningFeedback` | `0x4F750` | 20,144 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 110 | *Ordinal Only* | `0x54600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 144 | *Ordinal Only* | `0x54610` | 96 | UnwindData |  |
| 52 | `DllCanUnloadNow` | `0x54D60` | 129 | UnwindData |  |
| 53 | `DllGetActivationFactory` | `0x54DF0` | 134 | UnwindData |  |
| 54 | `DllGetClassObject` | `0x54E80` | 152 | UnwindData |  |
| 145 | *Ordinal Only* | `0x57150` | 57 | UnwindData |  |
| 118 | *Ordinal Only* | `0x57250` | 28 | UnwindData |  |
| 100 | *Ordinal Only* | `0x57280` | 48 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 124 | *Ordinal Only* | `0x572B0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 105 | *Ordinal Only* | `0x572C0` | 25 | UnwindData |  |
| 130 | *Ordinal Only* | `0x572E0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 102 | *Ordinal Only* | `0x572F0` | 30 | UnwindData |  |
| 97 | *Ordinal Only* | `0x57320` | 37 | UnwindData |  |
| 111 | *Ordinal Only* | `0x575B0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 113 | *Ordinal Only* | `0x575D0` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 108 | *Ordinal Only* | `0x575E0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 112 | *Ordinal Only* | `0x57600` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 107 | *Ordinal Only* | `0x57610` | 31 | UnwindData |  |
| 109 | *Ordinal Only* | `0x57640` | 3,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 143 | *Ordinal Only* | `0x583F0` | 42 | UnwindData |  |
| 141 | *Ordinal Only* | `0x58420` | 42 | UnwindData |  |
| 142 | *Ordinal Only* | `0x58450` | 1,872 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 90 | *Ordinal Only* | `0x58BA0` | 540 | UnwindData |  |
| 12 | `BeginPanningFeedback` | `0x5B0D0` | 21,504 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 64 | *Ordinal Only* | `0x604D0` | 185 | UnwindData |  |
| 46 | *Ordinal Only* | `0x60600` | 118 | UnwindData |  |
| 115 | *Ordinal Only* | `0x60680` | 30 | UnwindData |  |
| 86 | *Ordinal Only* | `0x60A00` | 128 | UnwindData |  |
| 127 | *Ordinal Only* | `0x60A90` | 93 | UnwindData |  |
| 116 | *Ordinal Only* | `0x60B00` | 928 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 67 | *Ordinal Only* | `0x60EA0` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 60 | *Ordinal Only* | `0x60EC0` | 181 | UnwindData |  |
| 15 | *Ordinal Only* | `0x60F80` | 16 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 103 | `EnableTheming` | `0x60F90` | 39 | UnwindData |  |
| 36 | *Ordinal Only* | `0x60F90` | 39 | UnwindData |  |
| 8 | *Ordinal Only* | `0x60FC0` | 752 | UnwindData |  |
| 149 | `GetBufferedPaintTargetRect` | `0x612C0` | 130 | UnwindData |  |
| 7 | *Ordinal Only* | `0x61350` | 254 | UnwindData |  |
| 160 | `GetThemeDocumentationProperty` | `0x61460` | 177 | UnwindData |  |
| 162 | `GetThemeFilename` | `0x61520` | 200 | UnwindData |  |
| 165 | `GetThemeIntList` | `0x615F0` | 163 | UnwindData |  |
| 48 | *Ordinal Only* | `0x616A0` | 61 | UnwindData |  |
| 173 | `GetThemeString` | `0x616F0` | 214 | UnwindData |  |
| 176 | `GetThemeSysColorBrush` | `0x617D0` | 208 | UnwindData |  |
| 178 | `GetThemeSysInt` | `0x618B0` | 152 | UnwindData |  |
| 180 | `GetThemeSysString` | `0x61950` | 189 | UnwindData |  |
| 73 | *Ordinal Only* | `0x61A20` | 81 | UnwindData |  |
| 50 | *Ordinal Only* | `0x61A80` | 223 | UnwindData |  |
| 191 | `IsThemeDialogTextureEnabled` | `0x61B70` | 126 | UnwindData |  |
| 17 | *Ordinal Only* | `0x61C00` | 107 | UnwindData |  |
| 1 | *Ordinal Only* | `0x61C80` | 169 | UnwindData |  |
| 14 | *Ordinal Only* | `0x61D30` | 332 | UnwindData |  |
| 68 | *Ordinal Only* | `0x61E90` | 32 | ContiguousDelta | *Size estimated via contiguous RVA delta.* |
| 65 | *Ordinal Only* | `0x61EB0` | 248 | UnwindData |  |
