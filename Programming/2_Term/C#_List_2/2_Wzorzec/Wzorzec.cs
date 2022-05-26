namespace Wzorzec;

public class Wzorzec
{
    private String _napis;
    private String _pattern;
    private List<int> _pozycje = new List<int>();
    public Wzorzec(String p, String n)
    {
        _pattern = p;
        _napis = n;
    }

    public void SzukajPozycje()
    {
        if (_napis.Length < _pattern.Length)
        {
            Console.Write(_pozycje);
        }
        else
        {
            int charactersFound = 0;
            for (int i = 0; _napis.Length > i; i++)
            {
                if (charactersFound == _pattern.Length)
                {
                    _pozycje.Add(i-_pattern.Length);
                    charactersFound = 0;
                }
                
                if (_napis[i] == _pattern[charactersFound])
                {
                    charactersFound++;
                }
            }
        }
       
    }

    public override string ToString()
    {
        String pokaz = "";
        Console.WriteLine($"Wzorzec: {_pattern}");
        foreach (char literka in _napis)
        {
            pokaz+=$"{literka} ";
        }

        pokaz += "\n";

        int index = 0;
        for (int i = 0; _napis.Length > i; i++)
        {
            if (_pozycje[index] != i)
            {
                pokaz+="--";
            }
            else if (_pozycje.Count - 1 >= index) // 0 1 - 2
            {
                if (_pozycje[index] < 10) pokaz+= $"{i}-";
                else pokaz += i.ToString();
                
                if (index != _pozycje.Count - 1) index++;
            }
        }

        pokaz += "\n";
        
        return pokaz;
    }
}