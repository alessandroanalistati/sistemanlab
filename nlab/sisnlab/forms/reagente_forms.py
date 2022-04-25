from django import forms
from ..models import Reagente, Marca, Sala, Armario, Bancada, Estante, Prateleira, Gaveta, Unidade

class DateInput(forms.DateInput):
    input_type = 'date'    

class ReagenteForm(forms.ModelForm):
       
    class Meta:
        model = Reagente
        fields = ['usuario', 'nome', 'formula_q', 'grau_p', 'unidade', 'marca', 'quantidade', 'data_validade', 'controle_pfex', 'ficha_tec', 
        'massamolecular', 'densidade', 'disponibilidade', 'sala', 'armario', 'bancada', 'estante', 'prateleira', 'gaveta', 'obs', 'foto']
        
           
        widgets = {
            'data_validade': DateInput()
        }    
    


        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['armario'].queryset = Armario.objects

            if 'sala' in self.data:
                try:
                    sala_id = int(self.data.get('sala'))
                    self.fields['armario'].queryset = Armario.objects.filter(sala_id=sala_id)
                except (ValueError, TypeError):
                    pass  
            elif self.instance.pk:
                self.fields['armario'].queryset = self.instance.sala.armario_set.order_by('name')
                
                
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['estante'].queryset = Estante.objects        

            if 'sala' in self.data:
                try:
                    sala_id = int(self.data.get('sala'))
                    self.fields['estante'].queryset = Estante.objects.filter(sala_id=sala_id)
                except (ValueError, TypeError):
                    pass  
            elif self.instance.pk:
                self.fields['estante'].queryset = self.instance.sala.estante_set.order_by('name')    
                
                
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['bancada'].queryset = Bancada.objects       

            if 'sala' in self.data:
                try:
                    sala_id = int(self.data.get('sala'))
                    self.fields['bancada'].queryset = Bancada.objects.filter(sala_id=sala_id)
                except (ValueError, TypeError):
                    pass  
            elif self.instance.pk:
                self.fields['bancada'].queryset = self.instance.sala.bancada_set.order_by('name')      
                 
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['prateleira'].queryset = Prateleira.objects       

            if 'armario' in self.data:
                try:
                    armario_id = int(self.data.get('armario'))
                    self.fields['prateleira'].queryset = Prateleira.objects.filter(armario_id=armario_id)
                except (ValueError, TypeError):
                    pass  
            elif self.instance.pk:
                self.fields['prateleira'].queryset = self.instance.armario.prateleira_set.order_by('name') 
                
                        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['gaveta'].queryset = Gaveta.objects    

            if 'armario' in self.data:
                try:
                    armario_id = int(self.data.get('armario'))
                    self.fields['gaveta'].queryset = Gaveta.objects.filter(armario_id=armario_id)
                except (ValueError, TypeError):
                    pass  
            elif self.instance.pk:
                self.fields['gaveta'].queryset = self.instance.armario.gaveta_set.order_by('name')     
                
   


class ReagenteFormExcluir(forms.ModelForm):
    class Meta:
        model = Reagente
        fields = ['usuario', 'nome', 'formula_q', 'grau_p', 'unidade', 'marca', 'quantidade', 'data_validade', 'controle_pfex', 'ficha_tec', 
        'massamolecular', 'densidade', 'disponibilidade', 'sala', 'armario', 'bancada', 'estante', 'prateleira', 'gaveta', 'obs', 'foto']