Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;

public class Monitor {
    [DllImport("user32.dll")]
    public static extern IntPtr SendMessage(IntPtr hWnd, int Msg, IntPtr wParam, IntPtr lParam);
}
"@

Start-Sleep -Milliseconds 800

[Monitor]::SendMessage([intptr]0xffff, 0x0112, [intptr]0xF170, [intptr]2)